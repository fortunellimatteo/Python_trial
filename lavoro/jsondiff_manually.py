file1=[
 {
    "name": "John Wood",
    "age": 35,
    "country": "USA"
 },
 {
    "name": "Mark Smith",
    "age": 30,
    "country": "USA"
 }
]
file2=[
 {
    "name": "John Wood",
    "age": 35,
    "country": "USA"
 },
 {
    "name": "Mark Smith",
    "age": 30,
    "country": "USA"
 },
 {
    "name": "Oscar Bernard",
    "age": 25,
    "country": "Australia"
 }
]

for item in file2:
    if item['name'] not in [x['name'] for x in file1]:
        print(f"Found difference: {item}")
        file1.append(item)

print(f"New file1: {file1}")