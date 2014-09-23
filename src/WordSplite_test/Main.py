import Get_day_data
import Get_keywords
import Get_keynews
def main():
    for i in range(1,10):
        Get_day_data.TransforData(i)
        Get_day_data.TransforDataset(i)
        Get_keywords.Get_keywords(i)
        Get_keynews.Get_keynews(i)



main()    