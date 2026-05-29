company = {
        "Chairman" : "Dhafer",
        "ceo": "Ahmed",
        "departments": {
            "engineering": {
                "manager": "Sara",
                "team_size": 12,
                "projects": ["Backend API", "Mobile App"],
            },
            "design": {
                "manager": "Omar",
                "team_size": 5 ,
                "projects": ["Website Redesign"],
            },
        },
    }
print(company["Chairman"])
print(company["ceo"])
print(company["departments"]["engineering"]["manager"])
print(company["departments"]["design"]["team_size"])
print(company["departments"]["engineering"]["projects"][0])
print(company["departments"]["engineering"]["team_size"] + company["departments"]["design"]["team_size"])
# company["departments"]["design"] = 6 || This line must be froozen to make sure that it won't affect the final and expected output
print(company["departments"]["design"])
company["departments"]["marketing"]= ({"manager": "lina", "team_size" : 3, "projects":""})
print(company["departments"]["marketing"])
print(company)
print(f'''
Chairman : {company["Chairman"]},
CEO : {company["ceo"]},
Engineering manager : {company["departments"]["engineering"]["manager"]},
Design team size : {company["departments"]["design"]["team_size"]}
First engineering project : {company["departments"]["engineering"]["projects"][0]}
Total team size: {company["departments"]["engineering"]["team_size"] + company["departments"]["design"]["team_size"]}
Marketing : {company["departments"]["marketing"]}''')