#Create a function password() that returns access granted/denied if a given variable p equals the secret password "Knights19"
def password(p):
    if p == "Knights19":
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"