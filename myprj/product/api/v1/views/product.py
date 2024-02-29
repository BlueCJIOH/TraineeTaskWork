import datetime

from django.db.models import Count
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from activity.api.v1.serializers.activity import ActivitySerializer
from group.models import Group
from product.api.v1.serializers.product import ProductSerializer
from product.api.v1.services.product import distribute_members
from product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=["post"], url_path="access")
    def get_access(self, request, pk=None):
        """
        getting access to the product, joining a group following the rules
        """
        instance = self.get_object()
        if not (
            Product.objects.prefetch_related("members")
            .filter(members__id=request.user.id, pk=pk)
            .exists()
        ):
            group_cnt = instance.groups.count()
            member_sup = instance.max_members * group_cnt
            member_inf = instance.min_members * group_cnt
            all_members = list(
                Group.objects.prefetch_related("members")
                .filter(product_id=pk)
                .exclude(**{"members": None})
                .values_list("members", flat=True)
            )
            all_members.append(request.user.id)
            member_num = len(all_members)
            is_started = instance.start_date <= datetime.datetime.now(
                instance.start_date.tzinfo
            )
            if member_num < member_inf:
                Group.objects.prefetch_related("members").filter(
                    product_id=pk
                ).first().members.add(request.user.id)
            elif member_inf <= member_num <= member_sup and is_started:
                Group.objects.prefetch_related("members").annotate(
                    member_cnt=Count("members")
                ).filter(
                    product_id=pk, member_cnt__lt=instance.max_members
                ).first().members.add(
                    request.user.id
                )
            elif member_inf <= member_num <= member_sup and not is_started:
                distribute_members(
                    pk,
                    instance.min_members,
                    all_members,
                    member_num,
                    group_cnt,
                )
            else:
                group = Group.objects.create(
                    name=f"{instance.name}_{group_cnt + 1}", product_id=pk
                )
                if member_num > member_sup and is_started:
                    group.members.add(request.user.id)
                else:
                    distribute_members(
                        pk,
                        instance.min_members,
                        all_members,
                        member_num,
                        group_cnt + 1,
                    )
            instance.members.add(request.user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, methods=["get"], url_path="activities")
    def list_activity(self, request, pk=None):
        """
        list all activities belonging to this product
        """
        # without pagination
        queryset = self.get_object().activity_set.all()
        serializer = ActivitySerializer(queryset, many=True)
        return Response(serializer.data)
