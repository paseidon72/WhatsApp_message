from icrawler.builtin import GoogleImageCrawler


def google_img_downloader():
    filters = dict(
        type='photo',
        color='bleckandwhite',
        size='large',
        #license='noncommercial, commercial',
        #date=((2020, 1, 1), (2022, 5, 14))
    )
    crawler = GoogleImageCrawler(storage={'root_dir': './img'})
    # crawler.crawl(keyword='mr.robot', max_num=5)
    # crawler.crawl(keyword='spongebob', max_num=5, min_size=(1000,1000), overwrite=True)
    # crawler.crawl(
    #     keyword='Miami Florida',
    #     max_num=5,
    #     min_size=(1000,1000),
    #     overwrite=True,
    #     file_idx_offset='auto'
    # )
    crawler.crawl(
        keyword='New York',
        max_num=5,
        min_size=(1000, 1000),
        overwrite=True,
        file_idx_offset='auto'
    )

def main():
    google_img_downloader()


if __name__ == '__main__':
    main()
