def find_missing(arr1,arr2):

    if arr1 == arr2:

        return 0

    elif arr1 != arr2:

        x = set(arr1)

        y = set(arr2)

        z = x^y

        return list(z)[0]