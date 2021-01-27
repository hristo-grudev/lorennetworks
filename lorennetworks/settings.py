BOT_NAME = 'lorennetworks'

SPIDER_MODULES = ['lorennetworks.spiders']
NEWSPIDER_MODULE = 'lorennetworks.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'lorennetworks.pipelines.LorennetworksPipeline': 100,

}