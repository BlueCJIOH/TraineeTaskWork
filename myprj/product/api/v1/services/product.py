from group.models import Group


def distribute_members(
    product_id: int,
    min_: int,
    all_members,
    member_num: int,
    group_cnt: int,
) -> None:
    groups = (
        Group.objects.select_related("product")
        .prefetch_related("members")
        .filter(product_id=product_id)
    )
    for group in groups:
        group.members.clear()
        group.members.add(*[all_members.pop(0) for _ in range(min_)])
    remaining_members = member_num - min_ * group_cnt
    for idx in range(remaining_members):
        groups[idx % group_cnt].members.add(all_members.pop(0))
