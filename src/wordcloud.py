from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(abstract_list):

    abstract_num = 0
    entity_list = []
    #extract_num = 0

    while abstract_num < len(abstract_list):
        extract_num = 0
        while extract_num < len(abstract_list[abstract_num][1]):
            entity_list.append(abstract_list[abstract_num][1][extract_num][0])
            extract_num = extract_num + 1        
        abstract_num += 1

    cloud_text = ' '.join(entity_list)    

    # Create and generate a word cloud image:
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(cloud_text)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()