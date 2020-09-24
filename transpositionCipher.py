def transposition(message, key):
    if key == 1 or key > len(message) / 2:
        return "Invalid key"

    output = [''] * key

    col = 0
    for m in message:
        output[col] += m
        col = col + 1

        if col  >= key:
            col = 0

    return ''.join(output)


message = "Having run through different yards and side streets, Pierre got back with his little burden to the Gruzinski garden at the corner of the Povarskoy. He did not at first recognize the place from which he had set out to look for the child, so crowded was it now with people and goods that had been dragged out of the houses. Besides Russian families who had taken refuge here from the fire with their belongings, there were several French soldiers in a variety of clothing. Pierre took no notice of them. He hurried to find the family of that civil servant in order to restore the daughter to her mother and go to save someone else. Pierre felt that he had still much to do and to do quickly. Glowing with the heat and from running, he felt at that moment more strongly than ever the sense of youth, animation, and determination that had come on him when he ran to save the child. She had now become quiet and, clinging with her little hands to Pierre's coat, sat on his arm gazing about her like some little wild animal. He glanced at her occasionally with a slight smile. He fancied he saw something pathetically innocent in that frightened, sickly little face."
key = 156

print(transposition(message, key))