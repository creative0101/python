# Construct an interpreter for file formats

#input
name = input("Name of file,please. ")

#remove spaces no case-sensitivity
name = name.strip().lower()

# outputs media type according to ending
if name.endswith(".gif"):
    print("image/gif")
elif name.endswith(".jpg"):
    print("image/jpeg")
elif name.endswith(".jpeg"):
    print("image/jpeg")
elif name.endswith(".png"):
    print("image/png")
elif name.endswith(".pdf"):
    print("application/pdf")
elif name.endswith(".txt"):
    print("text/plain")
elif name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")