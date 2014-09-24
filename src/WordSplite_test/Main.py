import Get_day_data
import Get_keywords
import Get_keynews
import Delete_Repeat
import Get_hot_result
def main():
    for i in range(1,32):
        Get_day_data.TransforData(i)
        Get_day_data.TransforDataset(i)
        Get_keywords.Get_keywords(i)
        Get_keynews.Get_keynews(i)
    Delete_Repeat.Delete_Repeat()
    Get_hot_result.get_hot_result(100)

main()    