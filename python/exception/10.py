
def convert_to_float(str_list):
    float_list = []
    error_list = []
    
    for string in str_list:
        try:
            float_value = float(string)
            float_list.append(float_value)
        except ValueError as err:
            error_list.append((string, str(err)))
        except Exception as e:
            error_list.append((string, str(e)))
    return float_list, error_list

def main():
    str_list = ['3.5', '4', '8.2', '7', 'a']
    float_list, error_list = convert_to_float(str_list)
    print(f"{float_list=},\n{error_list=}")


if __name__ == '__main__':
    main()