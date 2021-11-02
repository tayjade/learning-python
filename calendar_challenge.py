'''
Exercise:
    https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true



Calendar Module
    The calendar module allows you to output calendars and provides additional useful functions for them.

    class calendar.TextCalendar([firstweekday])

    This class can be used to generate plain text calendars.
    
    NOTE: To learn more about the calendar library, please visit (https://docs.python.org/3/library/calendar.html)

Sample Code:
    >>> import calendar
    >>>
    >>> print(calendar.TextCalendar(firstweekday=6).formatyear(2022))
                                    2022

        January                   February                   March
    Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
                    1             1  2  3  4  5             1  2  3  4  5
    2  3  4  5  6  7  8       6  7  8  9 10 11 12       6  7  8  9 10 11 12
    9 10 11 12 13 14 15      13 14 15 16 17 18 19      13 14 15 16 17 18 19
    16 17 18 19 20 21 22      20 21 22 23 24 25 26      20 21 22 23 24 25 26
    23 24 25 26 27 28 29      27 28                     27 28 29 30 31
    30 31

        April                      May                       June
    Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
                    1  2       1  2  3  4  5  6  7                1  2  3  4
    3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
    10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
    17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
    24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30

            July                     August                  September
    Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
                    1  2          1  2  3  4  5  6                   1  2  3
    3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
    10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
    17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
    24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
    31

        October                   November                  December
    Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
                    1             1  2  3  4  5                   1  2  3
    2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
    9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
    16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
    23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
    30 31

    >>>



Task: 
    You are given a date. Your task is to find what the day is on that date.

Input Format:

    A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

Constraints:

    2000 < year < 3000

Output Format:

    Output the correct day in capital letters.

Sample Input:
    
    08 05 2015

Sample Output:

    WEDNESDAY
'''
