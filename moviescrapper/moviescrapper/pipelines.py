# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MoviescrapperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name == "movie_rating":
                value = adapter.get(field_name)
                if value is not None:
                    new_value= value.replace(" / 10", "").strip()
                    movie_rate = float(new_value)
                    adapter[field_name] = movie_rate

        for field_name in field_names:
            if field_name == "movie_release_year":
                value = adapter.get(field_name)
                new_value = int(value)
                adapter[field_name] = new_value

        return item
