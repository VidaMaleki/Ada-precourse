for field_item in ["grass", "grass", "more grass", "rocks", "rocks", "more rocks"]:
    print("...")
    if field_item == "four-leaf clover":
        print("I found a four-leaf clover!")
        print("My hunt is over! I can leave now")
        break
    print(f"I found {field_item} in the field...")
    print("Better keep looking.")
else:
    print("I didn't find a four-leaf clover today.")

