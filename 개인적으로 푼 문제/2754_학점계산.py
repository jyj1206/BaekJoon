n=input()

def grade(n):
  ans=0
  if n[0]=='A':
    ans=4
  elif n[0]=='B':
    ans=3
  elif n[0]=='C':
    ans=2
  elif n[0]=='D':
    ans=1
  else:
    print(f'{ans:.1f}')
    return
  
  if n[1]=='+':
    ans+=0.3
  elif n[1]=='-':
    ans-=0.3
  
  print(f'{ans:.1f}')
  
grade(n)