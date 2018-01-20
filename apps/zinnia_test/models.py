from django.db import models
from zinnia.models_bases.entry import Entry



class EntryGallery(
          entry.CoreEntry,
          entry.ContentEntry,
          entry.DiscussionsEntry,
          entry.RelatedEntry,
          entry.ExcerptEntry,
          entry.FeaturedEntry,
          entry.AuthorsEntry,
          entry.CategoriesEntry,
          entry.TagsEntry,
          entry.LoginRequiredEntry,
          entry.PasswordRequiredEntry,
          entry.ContentTemplateEntry,
          entry.DetailTemplateEntry):


    class Meta(entry.CoreEntry.Meta):
        abstract = True