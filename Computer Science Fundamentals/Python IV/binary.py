# "1001" in base ten represents "1 thousand, 0 hundreds, 0 tens, and 1 one."
# It is base 10.
# In decimal there can be upto 9 of each.

# Each successive digit in the base 10 number system is a power of ten. The ones place is 10^0 = 1. The tens place is 10^1 = 10. The hundreds place is 10^2 = 100. This pattern continues on and on.

# This pattern holds for other number systems as well. In the binary system (base 2), each successive digit represents a different power of 2. The first digit represents 2^0 = 1. The second digit represents 2^1 = 2. The third digit represents 2^2 = 4. Again, this pattern continues on and on.

# In binary there can only be upto one of each.

# The word binary comes from "Bi-" meaning two. We see "bi-" in words such as "bicycle" (two wheels) or "binocular" (two eyes).
# A single binary digit (like "0" or "1") is called a "bit".
# The word bit is made up from the words "binary digit"!

# So, what if the number "1001" was in binary and not decimal? What would it represent then? Well, if we read it right to left, we have a "1" in the ones place, a "0" in the twos place, a "0" in the fours place, and a "1" in the eights place. We add these values up (8 + 0 + 0 + 1) which equals 9.

# Decimal	Binary
# 0	0000
# 1	0001
# 2	0010
# 3	0011
# 4	0100
# 5	0101
# 6	0110
# 7	0111
# 8	1000
# ...
# 15 1111 (half a byte (a nibble) has 16 possibilities. In hex you can represent 16 possibilities in one character from 0 to f)

# https://www.mathsisfun.com/binary-number-system.html

# The "10" means 2 in decimal,
# The ".1" means half,
# So "10.1" in binary is 2 + 1/2 or 2.5 in decimal

# I guess you don't call it a decimal place if you're working in binary
# You can refer to this symbol as a radix point no matter what the base is.
# In computer science and mathematics, the word radix can mean the same thing as base or root.
# In binary, the point can also be referred to as a binary point

# As we move further left, every number place gets 2 times bigger (multiplied by 2 - increasing the power once more means multiplied by another 2).
# As we move further right, every number place gets 2 times smaller (divided by 2).

# So to the right of the decimal you're doing 1/2, 1/4, 1/8 etc.

# This is the same in base 10 which gets 10x bigger (increasing the power means multiplied by another 10) to the left of the decimal or divided by 10 to the right of the decimal.
# in base 10, 10.1 means 10 + 1/10

# We now know that things are stored in RAM using binary, and each "box" in RAM holds 1 byte (8 bits). What does that mean for what we can store in RAM? Let's say we have 1 byte of RAM to use. How many different numbers can we represent using only this 1 byte?

# Remember that each digit in a binary number is a successive power of 2. If we have 8 bits to use, we can store 2^8 = 256 different numbers in 1 byte.

# NOTE this is not the same as storing the actual number 256, which would require 9 bits. It means that with 8 bits (a byte) you can store the numbers from 0-255. 256 different numbers.

# Unsigned integers are represented as a sequence of N bits, thus being able to represent numbers between 0 and 2^N-1. 
# An unsigned 8-bit integer can store any value between 0 and 255, an unsigned 16-bit integer can store any value between 0 and 65535

# Remember that because the first bit represents 2^0, which is 1, the 8th bit represents 2^7, which is 128
# Maybe remember this as being like zero based indexing. The first position represents 2^0.

# 128 = 10000000
# 255 = 11111111
# 256 = 100000000

# Filling up all digits to the right of a bit with be 1 less than that bit represents.

# Every time we add a new bit, we double the number of possible numbers we can express in binary. 
# This pattern can be generalized as 2^n and 2^8 = 256.

# This is the same as every new digit of base 10 we multiply the number of possible numbers we can store by 10.

# NOTE Don't get confused between the headings of which number each place represents starts at 2^0 (first place represents 1, next place is 2^1 which represents 2)
# and the way you calculate how many possible numbers you can store which starts with 2^1 (two possible numbers with one bit)
# Remember that either way it's base 2 with increasing exponents (not increasing bases squared!). Binary is a base 2 number system.


# https://www.technipages.com/32-bit-vs-64-bit-cpus#:~:text=For%20three%20bits%2C%20you%20have,total%20of%2018%2C446%2C744%2C073%2C709%2C551%2C616%20possible%20values.

# ^good piece on 32-bit vs 64-bit CPUs
# A 32bit-CPU is only capable of using 32-bit registers to store data and processing 32-bit values.
# Tip: A register is a piece of extremely fast memory that stores the data that the CPU is actively working on.
# The main limitation of a 32-bit CPU is the amount of RAM it can support. 
# A 32-bit CPU can only address up to 4 GiB of RAM, a 32-bit CPU is physically not capable of calling the address of any RAM above this amount. 

# In order of speed it must be:
# Storage --> Memory (RAM) --> Cache --> Register
# Each closer to the processor than the last

# Tip: GiB means Gibibytes. Gibi is a prefix designed for binary systems like computers and is designed to allow for the fact that the standard prefix of giga (1,000,000,000) is not a whole number in binary. In this prefix notation, each stage of prefix is 1024 times larger than the previous one, rather than 1000 times. For example, one kilogram is 1000 grams and one kibibyte is 1024 bytes. Four gibibytes is 4 x 1024 x 1024 x 1024 bytes, or 4,294,967,296 bytes.

# At 32-bits (4 bytes), you have 232 possible combinations or 4,294,967,296 possible values.
# With 64 bits 8 (bytes), there are a total of 18,446,744,073,709,551,616 possible values

# https://www.quora.com/Will-there-ever-be-another-128-bit-video-game-console

# ^ In videogame consoles

# The 2^X in the binary number system is called the bitsize. Eight bytes of memory are called "8-bit", and 16 bytes are called "16-bit," etc.
# ???? does it mean 8 bits and 16 bits ????

# In theory, you could use less space to represent smaller integers. For instance, in binary, the number one is represented by 1. So, technically, to store one in binary, you only need one bit. But computers don't usually do this. Many integers take a fixed amount of space, no matter what number they might have in them. So, even though you only need one bit to represent the number one, the computer would still use 32 or 64 bits to do so.

# So, if a variable represents a fixed-width integer, it doesn't matter if it has the value 0 or 123,456; the amount of space it takes up in RAM is the same.

# The computer can store numbers like 3, 60000000, or -14 in 32 bits, one of the "fixed-width integers" we discussed earlier. All of these fixed-width integers take up constant space (O(1)).

# Storing numbers as fixed-width integers introduces a trade-off. We have constant space complexity, and because each integer has a constant and expected number of bits, simple mathematical operations only take constant time. The cost of having an integer as fixed-width is that there is a limit to the number of integers you can represent.


# So, let's say we wanted to write a program that allowed us to keep track of the number of hours we spent studying that day. We will round the number of hours to the nearest whole number to store them as fixed-width integers. Additionally, each day's hours will be represented by eight bits in binary.

# So, we will start at memory address 0 in RAM, and each day, store the number of hours we studied in that "box" of RAM. For our first day that we are tracking, we store an 8-bit binary integer in "box" number 0. On the second day, we store an 8-bit binary integer in "box" number 1. This pattern continues.

# Now, I'm sure you've already used an array when you are programming. An array is just an ordered sequential collection of data. Well, RAM is already structured like this. Right? Our days where we track the number of hours that we are studying are in sequential order in RAM.

# Knowing this information, what can we do if we want to look up how many hours we studied on day 5 (index 4 because of zero-indexing)? Because all of the information is stored in sequential order, we can do simple math. If you are looking for the day 5 information (index 4), you need to know what the starting item address is 0 and then add 4 (the index). Or, if the starting address was 5 and you were looking for the 10th index, you'd go to memory address 15 (5 + 10).

# This math works because we are using one "box" in memory for each day's record. If we were using 64-bit integers that take up 8 "boxes" in RAM, we would have to slightly adjust our math. In this case, we would have to multiply the index we were looking for by the number of bytes each record was stored in. So, if we were storing 64-bit integers (8 bytes) and wanted to find the item with index 4, and the starting index was 0, we would go to memory address 0 + (4 * 8) = 32.

# Because accessing information from a specific index involves this simple mathematical computation, accessing items in an array is a constant time operation. For the mathematical computations to be consistent and straightforward, arrays have to follow specific rules. Each item in the array has to take up the same number of bytes in RAM. Also, each item has to be stored right next to the previous item in RAM. If there are any gaps or interruptions in the array, then the simple mathematical computation for accessing a particular item no longer works.


# In this example, we will store some strings. A string, as we know, is just a bunch of characters or letters. One straightforward way to store a string is an array, so let's see how we can define some mappings to make it easier to store strings in arrays.

# FOLLOW ALONG
# To use our 8-bit slots in memory, we need a way to encode each character in a string in 8-bits. One common character encoding to do this is called "ASCII". Here's how the alphabet is encoded in ASCII:

# Letter	Encoding
# A	01000001
# B	01000010
# C	01000011
# D	01000100
# E	01000101
# F	01000110
# G	01000111
# H	01001000
# I	01001001
# J	01001010
# K	01001011
# L	01001100
# M	01001101
# N	01001110
# O	01001111
# P	01010000
# Q	01010001
# R	01010010
# S	01010011
# T	01010100
# U	01010101
# V	01010110
# W	01010111
# X	01011000
# Y	01011001
# Z	01011010

# Since we can express characters as 8-bit integers, we can express strings as arrays of 8-bit characters.

# For example, we could represent LAMBDA like so:

# L -> 01001100
# A -> 01000001
# M -> 01001101
# B -> 01000010
# D -> 01000100
# A -> 01000001

# Each character, once it was encoded, could be stored as one 8-bit slot in memory.
# Note that ASCII is a 7-bit character set containing 128 characters, hence why the 8th bit is always set to 0.

# https://www.w3schools.com/charsets/ref_html_ascii.asp

# Table of all ASCII characters can be found in the link.

# ASCII stands for the "American Standard Code for Information Interchange".

# ASCII was the first character set (encoding standard) used between computers on the Internet.

# Both ISO-8859-1 (default in HTML 4.01) and UTF-8 (default in HTML5), are built on ASCII.

# ASCII is a 7-bit character set containing 128 characters.

# It contains the numbers from 0-9, the upper and lower case English letters from A to Z, and some special characters.

# The character sets used in modern computers, in HTML, and on the Internet, are all based on ASCII.

# ASCII Device Control Characters
# The ASCII control characters (range 00-31, plus 127) were designed to control hardware devices.
# Control characters (except horizontal tab, line feed, and carriage return) have nothing to do inside an HTML document.


# In computing, a nibble (occasionally nybble or nyble to match the spelling of byte) is a four-bit aggregation, or half an octet. It is also known as half-byte or tetrade. In a networking or telecommunication context, the nibble is often called a semi-octet, quadbit, or quartet. 

# A nibble has sixteen possible values (2^4). 
# A nibble can be represented by a single hexadecimal digit and called a hex digit.

# A full byte (octet) is represented by two hexadecimal digits; therefore, it is common to display a byte of information as two nibbles.
# Sometimes the set of all 256 byte values is represented as a 16×16 table, which gives easily readable hexadecimal codes for each value.


# https://vladris.com/blog/2018/10/13/arithmetic-overflow-and-underflow.html

# In C++
# x is an unsigned 16 bit integer, which can represent values between 0 and 65535. If x is 65535 and we increment it, the value becomes 65536 but that value cannot be represented by a uint16_t. This is an overflow. In this case, C++ wraps the value around and x becomes 0.

# similarly decrementing 0 is -1, which cannot be represented by an uint16_t and becomes 65535

# Python provides support for arbitrarily large integers: unlike C++, where the bit width (number of bits used to represent a number) is fixed, we can have integers of any size:
print(10**100)

# Why don’t all languages provide such support? The answer is performance. The underlying hardware the code runs on uses fixed-width integers, so performing arithmetic on fixed-width integer types becomes a single CPU instruction. 

# On the other hand, supporting arbitrarily large integers usually involves writing code to determine how many bits a given value or the result of an arithmetic operation needs and convert that into an array of fixed-width integers large enough to hold that value. The added overhead of this is non-trivial, so unlike Python, most other mainstream languages offer only fixed-width integers and support arbitrarily large integers only explicitly, via libraries.

# Unsigned integers
# Unsigned integers are represented as a sequence of N bits, thus being able to represent numbers between 0 and 2^N-1. An unsigned 8-bit integer can store any value between 0 and 255, an unsigned 16-bit integer can store any value between 0 and 65535, an unsigned 32-bit integer between 0 and 4294967295, and an unsigned 64-bit integer between 0 and 18446744073709551615.

# Unsigned integer representation is trivial.

