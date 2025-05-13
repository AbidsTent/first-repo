text = "X-DSPAM-Confidence:    0.8475"
start=text.find("0")
end = len(text)+1
print(text[start:end])
