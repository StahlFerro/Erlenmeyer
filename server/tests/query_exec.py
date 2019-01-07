# import sys
# sys.path.append('../..')
# from timeit import timeit
# from server import session
# from server.models import Ship
#
#
# x = "[record.id for record in Ship.query.all()]"
# y = "[id for id, in session.query(Ship.id).all()]"
#
# test1 = timeit(x, number=1000, globals=globals())
# test2 = timeit(y, number=1000, globals=globals())
#
# print('='*20)
# print(test1)
# print(test2)


def id_query_test():
    x = "[record.id for record in Ship.query.all()]"
    y = "[id for id, in session.query(Ship.id).all()]"

    test1 = timeit(x, number=1000, globals=globals())
    test2 = timeit(y, number=1000, globals=globals())
    print("=" * 10, "id query test", "="*10)
    print(test1)
    print(test2)


def sort_test():
    x = "j = [vars(record) for record in Ship.query.all()]\nj.sort(key=lambda i: i['id'])"
    test1 = timeit(x, number=1000, globals=globals())
    print("=" * 10, "sort test", "="*10)
    print(test1)


if __name__ == '__main__':
    import sys

    sys.path.append('../..')
    from timeit import timeit
    from server import session
    from server.models import Ship

    id_query_test()
    sort_test()

print(__name__)
