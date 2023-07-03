
def create_record(name, telephon, address):
    """Create record"""
    record = {
        'name': name,
        'phone': telephon,
        'address': address
    }
    return record

user1 = create_record("vasy", "+380000000", "Tula")
user2 = create_record("Petya", "+388800000", "ligaTula")

print(user1)
print(user2)

def give_award(medal, *persons):
    """Give Medal to persons"""
    for person in persons:
        print("Tovarish : " + person.title() + " Nagrajdaetsya medal " + medal)

give_award("Za Berlin", "Vasya", "Petya")
give_award("Za London", "Petya", "Alex", "Valentin")