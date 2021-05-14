from generate_land import ask_for_number, generate_land
import os


os.makedirs("outputs", exist_ok=True)


for i in range(1, 10):
    output = generate_land(20, 20)
    filename = os.path.join("outputs", f"test{i}.text")

    with open(filename, "w") as f:
        f.write(output)
