text = "X-DSPAM-Confidence:    0.8475"
t=text.strip()
pos=t.find(':')
print(t[pos+1:])
