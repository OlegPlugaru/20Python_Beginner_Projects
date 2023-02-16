# import urlib
# use urllib.request to get the data from the url

import urllib.request as urllib

# write a function that takes a url
def main(url):
    print("Checking connectivity ")

    # returns a response
    response = urllib.urlopen(url)
    print("Connected to", url, "succesfully")
    print("The response code was:", response.getcode())    

print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")

main(input_url)
    