class StringToFloat:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "data": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "str_to_float"
    CATEGORY = "utils"

    def str_to_float(self, data):
        return (float(data),)

class StringToInt:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "data": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "str_to_int"
    CATEGORY = "utils"

    def str_to_int(self, data):
        return (int(data),)


NODE_CLASS_MAPPINGS = {
    "StringToInt": StringToInt,
    "StringToFloat": StringToFloat,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StringToInt": "Convert String To Int",
    "StringToFloat": "Convert String To Float",
}

