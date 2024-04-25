import json
import os

class worldMap:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.segments = {}

    def add_segment(self, x, y, sprite_path):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.segments[(x, y)] = mapSegment(x, y, sprite_path)
        else:
            print("Invalid coordinates for map segment.")

    def to_dict(self):
        segments_dict = {f"segment_{i}": segment.__dict__ for i, segment in enumerate(self.segments.values())}
        return {
            "width": self.width,
            "height": self.height,
            "segments": segments_dict
        }

    def serializeMapData(self):
        folder_name = f"{self.name}_DATA"
        os.makedirs(folder_name, exist_ok=True)

        json_file_path = os.path.join(folder_name, "map.json")
        with open(json_file_path, "w") as file:
            json.dump(self.to_dict(), file, indent=4)

        for segment in self.segments.values():
            if segment.spritePath:
                sprite_file_name = os.path.basename(segment.spritePath)
                sprite_dest_path = os.path.join(folder_name, sprite_file_name)
                if os.path.exists(segment.spritePath):
                    os.replace(segment.spritePath, sprite_dest_path)
                else:
                    print(f"Sprite image '{segment.spritePath}' not found.")

class mapSegment:
    def __init__(self, x, y, spritepath):
        self.x = x
        self.y = y
        self.spritePath = spritepath

