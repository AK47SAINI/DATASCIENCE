class Alphabet:
    def count_vowels(self,stra):
        count=0
        for i in stra :
            if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U': 
                count+=1


        return count
a=Alphabet()
inputstring=input("Enter the String : ")
print("The Count of vowel in the given string is : ",a.count_vowels(inputstring))