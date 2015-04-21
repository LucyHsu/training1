import sys 


def name_score(non_order_list):
        list_sorted = sorted(non_order_list)
        A_offset = 64
        score_list = []
        for index, value in enumerate(list_sorted):
            sum = 0
            for char_in_value in value:
                sum += ord(char_in_value)-A_offset
            score_list.append(sum*(index+1))
        return score_list



#file_name = sys.argv[1]
#f = open(file_name)
#string_in_file = f.read().strip('"\n')  # => 'CDEF","ABC","FIJK'
#list_in_file = string_in_file.split('","')    # => ['CDEF', 'ABC', 'FIJK']
#scorelist = []
#scorelist = name_score(list_in_file)
#print scorelist

