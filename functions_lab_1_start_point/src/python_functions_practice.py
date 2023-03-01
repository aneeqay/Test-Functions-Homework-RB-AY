#   def test_return_10(self):
#       return_10_result = return_10()
#       self.assertEqual( 10, return_10_result )

def return_10():
    return 10
# ---------------------------------------------------------

# #   @unittest.skip("delete this line to run the test")
#   def test_add(self):
#       add_result = add( 1, 2 )
#       self.assertEqual( 3, add_result )

def add(first_no, second_no):
    return first_no + second_no
# ---------------------------------------------------------

#  @unittest.skip("delete this line to run the test")
#   def test_subtract(self):
#       subtract_result = subtract( 10, 5 )
#       self.assertEqual( 5, subtract_result )

def subtract(first_no, second_no):
    return first_no - second_no
# ---------------------------------------------------------

# def test_multiply(self):
#       multiply_result = multiply( 4, 2 )
#       self.assertEqual( 8, multiply_result )

def multiply(first_no, second_no):
    return first_no * second_no
# ---------------------------------------------------------

#   def test_divide(self):
#       divide_result = divide( 10, 2 )
#       self.assertEqual( 5, divide_result )

def divide(first_no, second_no):
    return first_no / second_no
# ---------------------------------------------------------

# def test_length_of_string(self):
#       string_length = length_of_string( "A string of length 21" )
#       self.assertEqual( 21, string_length )

def length_of_string(str):
    return len(str)
# ---------------------------------------------------------
#  def test_join_string(self):
#       string_1 = "Mary had a little lamb, "
#       string_2 = "its fleece was white as snow"
#       joined_string = join_string( string_1, string_2 )
#       self.assertEqual( "Mary had a little lamb, its fleece was white as snow", joined_string )

def join_string(line, line2):
    return line + line2

# ---------------------------------------------------------

#  def test_add_string_as_number(self):
#       add_result = add_string_as_number( "1", "2" )
#       self.assertEqual( 3, add_result )

def add_string_as_number(no_1, no_2):
    return int(no_1) + int(no_2)

# ---------------------------------------------------------

# def test_number_to_full_name__month_1(self):
#       result = number_to_full_month_name( 1 )
#       self.assertEqual( "January", result )

def number_to_full_month_name(number):
    list_of_months = {
        1 : "January",
        2 : "February",
        3 : "March",
        4 : "April",
        5 : "May",
        6 : "June",
        7 : "July",
        8 : "August",
        9 : "September",
        10 : "October",
        11 : "November",
        12 : "December"
    }
    return list_of_months[number]

# ---------------------------------------------------------

# def test_number_to_full_name__month_3(self):
#       result = number_to_full_month_name( 3 )
#       self.assertEqual( "March", result )

def number_to_full_month_name(number):
    list_of_months = {
        1 : "January",
        2 : "February",
        3 : "March",
        4 : "April",
        5 : "May",
        6 : "June",
        7 : "July",
        8 : "August",
        9 : "September",
        10 : "October",
        11 : "November",
        12 : "December"
    }
    return list_of_months[number]

# ---------------------------------------------------------
# def test_number_to_short_month_name__month_1(self):
#       first_month_string = number_to_short_month_name( 1 )
#       self.assertEqual( "Jan", first_month_string )

def number_to_short_month_name(number):
    list_of_months = {
        1 : "Jan",
        2 : "Feb",
        3 : "Mar",
        4 : "Apr",
        5 : "May",
        6 : "Jun",
        7 : "Jul",
        8 : "Aug",
        9 : "Sep",
        10 : "Oct",
        11 : "Nov",
        12 : "Dec"
    }
    return list_of_months[number]

# ---------------------------------------------------------

# def test_number_to_short_month_name__month_4(self):
#       fourth_month_string = number_to_short_month_name( 4 )
#       self.assertEqual( "Apr", fourth_month_string )

def number_to_short_month_name(number):
    list_of_months = {
        1 : "Jan",
        2 : "Feb",
        3 : "Mar",
        4 : "Apr",
        5 : "May",
        6 : "Jun",
        7 : "Jul",
        8 : "Aug",
        9 : "Sep",
        10 : "Oct",
        11 : "Nov",
        12 : "Dec"
    }
    return list_of_months[number]

# ---------------------------------------------------------

#  def test_number_to_short_month_name__month_10(self):
#       tenth_month_string = number_to_short_month_name( 10 )
#       self.assertEqual( "Oct", tenth_month_string )

def number_to_short_month_name(number):
    list_of_months = {
        1 : "Jan",
        2 : "Feb",
        3 : "Mar",
        4 : "Apr",
        5 : "May",
        6 : "Jun",
        7 : "Jul",
        8 : "Aug",
        9 : "Sep",
        10 : "Oct",
        11 : "Nov",
        12 : "Dec"
    }
    return list_of_months[number]
