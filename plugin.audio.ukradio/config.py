### ############################################################################################################
###	#	
### # Project: 			#		Config.py - by The Highway 2013.
### # Author: 			#		The Highway
### # Version:			#		(ever changing)
### # Description: 	#		My Project Config File
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs
import re,os,sys,string,StringIO,logging,random,array,time,datetime
from t0mm0.common.addon import Addon

### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
### Plugin Settings ###
def ps(x):
	return {
		'__plugin__': 					"RadioPlayer.co.uk"
		,'__authors__': 				"[COLOR white]The[COLOR tan]Highway[/COLOR][/COLOR]"
		,'__credits__': 				"TheHighway of plugin.video.theanimehighway for teh_tools.py, anilkuj of plugin.video.soloremovie (solarmovie.eu) for much initial work.  Mikey1234 of SimplyMovies.  Bstrdsmkr of 1 Channel.  Those that worked on UrlResolver.  Those of #XBMCHUB on irc.freenode.net.  And of course,  XBMCHub.com itself."
		,'_addon_id': 					"plugin.audio.ukradio"
		,'_plugin_id': 					"plugin.audio.ukradio"
		,'_domain_url': 				"http://www.radioplayer.co.uk"
		,'_image_url': 					"http://moviefork.com/posters/%s.jpg"
		,'_button_url':					"http://www.radioplayer.co.uk/wp-content/themes/radioplayer/images/logo-large.png"
		,'_fanart_url': 				"http://www.radioplayer.co.uk/wp-content/themes/radioplayer/images/background.jpg"
		,'_play_url': 					"http://moviefork.com/MovieDetails.cfm?Movie=%s"
		,'_category_url':				'http://moviefork.com/Results.cfm?%s'
		,'_database_name': 			"searchmp3mobi"
		,'_addon_path_art': 		"art"
		,'art_sun':							'http://moviefork.com/Images/fresh.png'
		,'art_dead':						'http://moviefork.com/Images/rotten.png'
		,'art_youtube':					'http://dc201.4shared.com/img/BOP7WPlc/s3/1394e9763e0/youtube-icon.png'
		,'special.home.addons': 'special:'+os.sep+os.sep+'home'+os.sep+'addons'+os.sep
		,'special.home': 				'special:'+os.sep+os.sep+'home'
		,'GENRES': 							['Action & Adventure','Animation','Art House & International','Classics','Comedy','Cult Movies','Documentary','Drama','Horror','Kids & Family','Musical & Performing Arts','Mystery & Suspense','Romance','Science Fiction & Fantasy','Special Interest','Sports & Fitness','Television']
		,'YEARS': 							['2010','2000','1990','1980','1970','1960','1950','1940','1930','1920']
		,'YEARSo': 							['1920','1930','1940','1950','1960','1970','1980','1990','2000','2010']
		,'GENRESo': 						['Action', 'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western']
		,'COUNTRIES': 					['Afghanistan','Albania','Algeria','Andorra','Angola','Argentina','Armenia','Aruba','Australia','Austria','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Bermuda','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Bulgaria','Cambodia','Cameroon','Canada','Chad','Chile','China','Colombia','Costa Rica','Croatia','Cuba','Cyprus','Czech Republic','Czechoslovakia','Democratic Republic of the Congo','Denmark','Dominican Republic','East Germany','Ecuador','Egypt','El Salvador','Estonia','Ethiopia','Federal Republic of Yugoslavia','Finland','France','Georgia','Germany','Ghana','Greece','Guatemala','Haiti','Honduras','Hong Kong','Hungary','Iceland','India','Indonesia','Iran','Ireland','Isle of Man','Israel','Italy','Jamaica','Japan','Kazakhstan','Kenya','Kuwait','Latvia','Lebanon','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Malaysia','Maldives','Malta','Mexico','Moldova','Monaco','Mongolia','Morocco','Namibia','Nepal','Netherlands','Netherlands Antilles','New Zealand','Nicaragua','Nigeria','North Korea','Norway','Occupied Palestinian Territory','Pakistan','Palestine','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Puerto Rico','Qatar','Republic of Macedonia','Romania','Russia','Rwanda','Senegal','Serbia','Serbia and Montenegro','Singapore','Slovakia','Slovenia','South Africa','South Korea','Soviet Union','Spain','Sri Lanka','Sweden','Switzerland','Taiwan','Tajikistan','Tanzania','Thailand','Togo','Trinidad and Tobago','Tunisia','Turkey','U.S. Virgin Islands','UK','Ukraine','United Arab Emirates','United States Minor Outlying Islands','Uruguay','USA','Venezuela','Vietnam','West Germany','Yugoslavia','Zaire','Zambia','Zimbabwe']
		,'RATINGS':							['G','PG','PG-13','NC-17','R','Unrated']
		,'SCORES':							['Bad','Below Average','Average','Above Average','Very Good','Great']
		,'default_art_ext': 		'.png'
		,'default_cFL_color': 	'lime'
		,'cFL_color': 					'lime'
		,'cFL_color2': 					'blue'
		,'cFL_color3': 					'red'
		,'cFL_color4': 					'grey'
		,'cFL_color5': 					'white'
		,'cFL_color6': 					'blanchedalmond'
		,'default_section': 		'movies'
		,'section.wallpaper':		'wallpapers'
		,'section.movie': 			'movies'
		,'section.trailers':		'trailers'
		,'section.trailers.popular':			'trailerspopular'
		,'section.trailers.releasedate':	'trailersreleasedate'
		,'section.users':				'users'
		,'section.tv': 					'tv'
		,'img.comingsoon': 			'http://mirror.its.dal.ca/xbmc/addons/frodo/plugin.video.trailer.addict/icon.png'
		,'img.usersection': 		'http://i1.wp.com/www.solarmovie.so/images/gravatar_default.png'
		,'img.userdefault': 		'http://i1.wp.com/www.solarmovie.so/images/gravatar_default.png'
		,'Trailers.GENRES': 		['All','Action', 'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western']
		,'meta.movie.domain': 	'http://www.themoviedb.org'
		,'meta.movie.search': 	'http://www.themoviedb.org/search?query=TT'
		,'meta.tv.domain': 			'http://www.thetvdb.com'
		,'meta.tv.search': 			'http://www.thetvdb.com/index.php?seriesname=&fieldlocation=2&language=7&genre=&year=&network=&zap2it_id=&tvcom_id=&order=translation&addedBy=&searching=Search&tab=advancedsearch&imdb_id=TT'
		,'meta.tv.page': 				'http://www.thetvdb.com/index.php?tab=series&lid=7&id='
		,'meta.tv.fanart.url': 	'http://www.thetvdb.com/banners/fanart/original/'
		,'meta.tv.fanart.url2': '-1.jpg'
		,'meta.tv.fanart.all.url': 'http://thetvdb.com/?tab=seriesfanart&id=%s'
		,'meta.tv.fanart.all.match':	'<a href="(banners/fanart/original/\d+-(\d+)\.jpg)" target="_blank">View Full Size</a>'
		,'meta.tv.fanart.all.prefix': 'http://thetvdb.com/'
		,'meta.tv.poster.url': 	'http://www.thetvdb.com/banners/posters/'
		,'meta.tv.poster.url2': '-1.jpg'
		,'domain.search.movie': 'http://www.solarmovie.so/movie/search/'
		,'domain.search.tv': 		'http://www.solarmovie.so/tv/search/'
		,'domain.url.tv': 			'/tv'
		,'domain.url.movie': 		''
		,'LatestThreads.url':		'http://www.solarmovie.so/'
		,'changelog.local': 		'changelog.txt'
		,'changelog.url': 			'https://raw.github.com/HIGHWAY99/plugin.video.solarmovie.so/master/changelog.txt'
		,'news.url': 						'https://raw.github.com/HIGHWAY99/plugin.video.solarmovie.so/master/news.txt'
		,'listSeasons.match.img': 				'coverImage">.+?src="(.+?)"'
		,'listSeasons.match.seasons': 		"toggleSeason\('(\d+)'\)"
		,'listSeasons.prefix.seasons': 		'[COLOR goldenrod]S[/COLOR]eason '
		,'setview.seasons': 							515
		,'setview.episodes': 							515
		,'setview.movies': 								515
		,'setview.tv': 										515
		,'setview.tv.latestepisodes': 		515
		,'domain.thumbnail.default': 			'http://static.solarmovie.so/images/movies/0000000_150x220.jpg'
		,'rating.max': 										'10'
		,'cMI.favorites.tv.add.url': 			'XBMC.RunPlugin(%s?mode=%s&section=%s&title=%s&year=%s&img=%s&fanart=%s&country=%s&plot=%s&genre=%s&url=%s&dbid=%s&subfav=%s)'
		,'cMI.favorites.tv.add.name': 		'Add Favorite'
		,'cMI.favorites.tv.add.mode': 		'FavoritesAdd'
		,'cMI.favorites.movie.add.url': 	'XBMC.RunPlugin(%s?mode=%s&section=%s&title=%s&year=%s&img=%s&fanart=%s&country=%s&plot=%s&genre=%s&url=%s&subfav=%s)'
		,'cMI.favorites.tv.remove.url': 	'XBMC.RunPlugin(%s?mode=%s&section=%s&title=%s&year=%s&img=%s&fanart=%s&country=%s&plot=%s&genre=%s&url=%s&dbid=%s&subfav=%s)'
		,'cMI.favorites.tv.remove.name': 	'Remove Favorite'
		,'cMI.favorites.tv.remove.mode': 	'FavoritesRemove'
		,'cMI.favorites.movie.remove.url': 'XBMC.RunPlugin(%s?mode=%s&section=%s&title=%s&year=%s&img=%s&fanart=%s&country=%s&plot=%s&genre=%s&url=%s&subfav=%s)'
		,'cMI.airdates.find.name': 				'Find AirDates'
		,'cMI.airdates.find.url': 				'XBMC.RunPlugin(%s?mode=%s&title=%s)'
		,'cMI.airdates.find.mode': 				'SearchForAirDates'
		,'cMI.showinfo.name': 						'Show Information'
		,'cMI.showinfo.url': 							'XBMC.Action(Info)'
		,'cMI.1ch.search.folder': 				'plugin.video.1channel'
		,'cMI.1ch.search.name': 					'Search 1Channel'
		,'cMI.1ch.search.url': 						'XBMC.Container.Update(%s?mode=7000&section=%s&query=%s)'
		,'cMI.1ch.search.plugin': 				'plugin://plugin.video.1channel/'
		,'cMI.1ch.search.section': 				'movies'
		,'cMI.1ch.search.section.tv': 		'tv'
		,'cMI.primewire.search.folder': 	'plugin.video.primewire'
		,'cMI.primewire.search.name': 		'Search PrimeWire.ag'
		,'cMI.primewire.search.url': 			'XBMC.Container.Update(%s?mode=7000&section=%s&query=%s)'
		,'cMI.primewire.search.plugin': 	'plugin://plugin.video.primewire/'
		,'cMI.primewire.search.section': 	'movies'
		,'cMI.primewire.search.section.tv':	'tv'
		,'cMI.jDownloader.addlink.url':		'XBMC.RunPlugin(plugin://plugin.program.jdownloader/?action=addlink&url=%s)'
		,'LI.movies.match.items': 				'class="coverImage" title="(.+?)".+?href="(.+?)".+?src="(.+?)".+?<a title=".+?\(([\d]+)\)'
		,'LI.movies.match.items2': 				'class="coverImage" title="(.+?)"[\n]\s+href="(.+?)">.+?src="(http://static\.solarmovie\.so/images/movies/\d+_\d+x\d+\.jpg)".+?<a\stitle=".+?\(([\d]+)\)'
		,'LI.movies.match.items3': 				'class="coverImage" title="(.+?)"[\n]\s+href="(.+?)">.+?src="(http://static\.solarmovie\.so/images/movies/\d+_\d+x\d+\.jpg)".+?<a\stitle=".+?\(([\d]+)\)'
		,'LI.movies.latest.split1': 			'<h2>Latest Movies</h2>'
		,'LI.movies.latest.split2': 			'<h2>'
		,'LI.movies.latest.check': 				'Latest'
		,'LI.movies.popular.new.split1': 	'<h2>Most Popular New Movies</h2>'
		,'LI.movies.popular.new.split2': 	'<h2>'
		,'LI.movies.popular.new.check': 	'NewPopular'
		,'LI.movies.popular.hd.split1': 	'<h2>Most Popular Movies in HD</h2>'
		,'LI.movies.popular.hd.split2': 	'<h2>'
		,'LI.movies.popular.hd.check': 		'HDPopular'
		,'LI.movies.popular.other.split1':'<h2>Other Popular Movies</h2>'
		,'LI.movies.popular.other.split2':'<h2>'
		,'LI.movies.popular.other.check': 'OtherPopular'
		,'LI.tv.latest.watched.check':		'LatestWatched'
		,'LI.tv.latest.match.items': 			'__(.+?) s(\d+)e(\d+) (.+?)__'
		,'LI.tv.latest.check': 						'Latest'
		,'LI.tv.latest.split1': 					'<h2>Most Popular New TV Shows</h2>'
		,'LI.tv.latest.split2': 					'<h3>'
		,'LI.tv.popular.all.check': 			'Popular'
		,'LI.tv.popular.all.split1': 			'<h2>Most Popular TV Shows</h2>'
		,'LI.tv.popular.all.split2': 			'<h2>'
		,'LI.tv.popular.new.check': 			'NewPopular'
		,'LI.tv.popular.new.split1': 			'<h2>Latest TV Shows</h2>'
		,'LI.tv.popular.new.split2': 			'<h3>'
		,'LI.tv.match.items': 						'class="coverImage" title="(.+?)".+?href="(.+?)".+?src="(.+?)".+?<a title=".+?\(([\d]+)\)'
		,'LI.nextpage.name': 							'  [COLOR goldenrod]>  [COLOR red]Next[/COLOR]...[/COLOR]'
		,'LI.nextpage.match': 						'<li class="next"><a href=.+?page=([\d]+)"'
		,'LI.nextpage.check': 						'<li class="next"><a href="http://www.solarmovie.so/'
		,'LI.page.param': 								'?page='
		,'LI.page.find': 									'<li><a href=.+?page=([\d]+)"'
		,'BrowseByYear.tv.url1': 					'/tv/watch-tv-shows-'
		,'BrowseByYear.tv.url2': 					'.html'
		,'BrowseByYear.movie.url1': 			'/watch-movies-of-'
		,'BrowseByYear.movie.url2': 			'.html'
		,'BrowseByGenre.tv.url1': 				'/tv/watch-'
		,'BrowseByGenre.tv.url2': 				'-tv-shows.html'
		,'BrowseByGenre.movie.url1': 			'/watch-'
		,'BrowseByGenre.movie.url2': 			'-movies.html'
		,'BrowseByYear.thisyear': 				2013
		,'BrowseByYear.earliestyear': 		1930
		,'BrowseByYear.range.by': 				-1
		,'Hosters.icon.url': 							'http://www.google.com/s2/favicons?domain='
		,'LLinks.compile.hosters': 				'<tr id=.+?href="(.+?)">(.+?)<.+?class="qualityCell">(.+?)<.+?<td class="ageCell .+?">(.+?)</td>'
		,'LLinks.compile.hosters2': 			'<tr id=.+?href="(/link/show/\d+/)">(.+?)<.+?class="qualityCell">(.+?)<.+?<td class="ageCell .+?">(.+?)</td>'
		,'LLinks.compile.imdb.url_id': 		'<strong>IMDb ID:</strong>[\n]\s+<a href="(.+?)">(\d+)</a>'
		,'LLinks.compile.show.plot': 			'<p id="plot_\d+">(.+?)</p>'
		,'LLinks.compile.show.title_year': '<title>Watch Full (.+?) \((.+?)\) .+?</title>'
		,'LLinks.compile.show_episode.info': '<title>Watch (.+?) Online for Free - (.+?) - .+? - (\d+)x(\d+) - SolarMovie</title>'
		,'AdvSearch.menu.0': 		'0.) Do Search >>'
		,'AdvSearch.menu.1': 		'1.) Title       '
		,'AdvSearch.menu.2': 		'2.) Description '
		,'AdvSearch.menu.3': 		'3.) Actor       '
		,'AdvSearch.menu.4': 		'4.) Country[N/A]'
		,'AdvSearch.menu.5': 		'5.) Year (From) '
		,'AdvSearch.menu.6': 		'6.) Year (To)   '
		,'AdvSearch.menu.7': 		'7.) Genre  [N/A]'
		,'AdvSearch.menu.8': 		'8.) Cancel      '
		,'AdvSearch.url.tv': 		'http://www.solarmovie.so/advanced-search/?'
		,'AdvSearch.url.movie': 'http://www.solarmovie.so/advanced-search/?'
		,'AdvSearch.tags.0': 		'is_series'
		,'AdvSearch.tags.1': 		'title'
		,'AdvSearch.tags.2': 		'actor'
		,'AdvSearch.tags.3': 		'description'
		,'AdvSearch.tags.4': 		'country'
		,'AdvSearch.tags.5': 		'year_from'
		,'AdvSearch.tags.6': 		'year_to'
		,'AdvSearch.tags.7': 		'genre'
		,'AdvSearch.tags.8': 		''
##		,'LLinks.compile.': 							
#		,'': 		''
#		,'': 
#		,'': 
	}[x]
_art_DefaultExt  ='.png'
_cFL_DefaultColor='goldenrod'

### Known Domains: 
### http://www.solarmovie.so
### http://www.solarmovie.eu
### http://solarmovies.com
### 
### 
### 
### 
### 
### 
### 
### 

### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
### For Multiple Methods ###

### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
### Other Settings ###
GENRES = ['Action', 'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western']
COUNTRIES = ['Afghanistan','Albania','Algeria','Andorra','Angola','Argentina','Armenia','Aruba','Australia','Austria','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Bermuda','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Bulgaria','Cambodia','Cameroon','Canada','Chad','Chile','China','Colombia','Costa Rica','Croatia','Cuba','Cyprus','Czech Republic','Czechoslovakia','Democratic Republic of the Congo','Denmark','Dominican Republic','East Germany','Ecuador','Egypt','El Salvador','Estonia','Ethiopia','Federal Republic of Yugoslavia','Finland','France','Georgia','Germany','Ghana','Greece','Guatemala','Haiti','Honduras','Hong Kong','Hungary','Iceland','India','Indonesia','Iran','Ireland','Isle of Man','Israel','Italy','Jamaica','Japan','Kazakhstan','Kenya','Kuwait','Latvia','Lebanon','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Malaysia','Maldives','Malta','Mexico','Moldova','Monaco','Mongolia','Morocco','Namibia','Nepal','Netherlands','Netherlands Antilles','New Zealand','Nicaragua','Nigeria','North Korea','Norway','Occupied Palestinian Territory','Pakistan','Palestine','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Puerto Rico','Qatar','Republic of Macedonia','Romania','Russia','Rwanda','Senegal','Serbia','Serbia and Montenegro','Singapore','Slovakia','Slovenia','South Africa','South Korea','Soviet Union','Spain','Sri Lanka','Sweden','Switzerland','Taiwan','Tajikistan','Tanzania','Thailand','Togo','Trinidad and Tobago','Tunisia','Turkey','U.S. Virgin Islands','UK','Ukraine','United Arab Emirates','United States Minor Outlying Islands','Uruguay','USA','Venezuela','Vietnam','West Germany','Yugoslavia','Zaire','Zambia','Zimbabwe']

### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
### Configurable Functions ###

### ############################################################################################################
