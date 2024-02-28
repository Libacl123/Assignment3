from db import district_lists

#CREATE

def create(new_dist):
 
  large_id = max(district['id'] for district in district_lists)
  new_dist["id"] = large_id + 1
  district_lists.append(new_dist)
  print("District list after adding:", district_lists)


#RETRIEVE

def retrieve(t_id):
 
  for district in district_lists:
    if district["id"] == t_id:
      return district
  return None


#UPDATE

def update(t_id, new_name):
  
  for i, district in enumerate(district_lists):
    if district["id"] == t_id:
      district["name"] = new_name
      print("District list after update:", district_lists)
      return
  print(f"District with ID {t_id}  is not found!!.")



#DELETE

def delete(t_id):
  
  for i, district in enumerate(district_lists):
    if district["id"] == t_id:
      del district_lists[i]
      print("District list after deletion:", district_lists)
      return
  print(f"District with ID {t_id} is not found!!.")
