global_flag = False
delete_global_value = True
delete_twice_value = True
delete_global_then_read_value = True


def set_flag_true():
    global global_flag
    global_flag = True


def set_flag_false():
    global global_flag
    global_flag = False


def delete_global_value_fn():
    global delete_global_value
    del delete_global_value


def delete_missing_global_value_fn():
    global delete_missing_global_value
    del delete_missing_global_value


def delete_twice_fn():
    global delete_twice_value
    del delete_twice_value
    # Deleting an already-deleted global raises NameError.
    del delete_twice_value  # noqa: F821


def delete_missing_then_store_fn():
    global delete_missing_then_store_value
    del delete_missing_then_store_value
    # Unreachable in eager, which raises on the line above; the store is here to
    # prove Dynamo does not replay it either.
    delete_missing_then_store_value = 5  # noqa: F841


def store_then_delete_missing_fn():
    global store_then_delete_missing_value
    store_then_delete_missing_value = 5
    del store_then_delete_missing_value


def delete_global_then_read_fn():
    global delete_global_then_read_value
    del delete_global_then_read_value
    # Reading a deleted global raises NameError.
    return delete_global_then_read_value  # noqa: F821
