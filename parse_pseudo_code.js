https://mynoise.net/superGenerator.php?
g
1=november2019SoundscapeGenerator.php%3Fc%3D3%26c%3D3&g
2=trafficNoiseGenerator.php%3Fc%3D3%26c%3D3&g
3=tropicalRainNoiseGenerator.php%3Fc%3D3%26c%3D3&g
4=propellerNoiseGenerator.php%3Fc%3D3%26c%3D3&g5=&yt=



todo:
validateSupergenUrl(url) {
  // confirm it is a supergen link with at least 2 generators
  does it start with http(s)://mynoise.net/superGenerator.php?
  does it contain more than three "Generator.php" (one for the base url, at least 2 generators)
  
  return new supergen { url: url }
}

ensureSoundExists(url) {
  sound = soundDictionary[url]
  if (sound) return sound
  
  // todo: scrape url for title
  sound = { url: url, title: title}
  soundDictionary[url] = sound
}

getSounds(url) {
  // todo: parse url for each <supergen-name>.php into an array
  forEach sound
    ensureSoundExists(url)
}

ensureSupergenAdded(defaultTitle, linkCount, url, redditUrl) {
  supergen = supergenDictionary.contains(url))
  if (supergen) 
    return true;
  
  if is link text !== url
    title = link text
  else if linkCount === 1
    title = defaultTitle
  else
    title = defaultTitle + index
  
  sounds = getSounds(url)
  
  supergen = { url: url, title: title, redditUrl: redditUrl, sounds: sounds }
}

scrapeSubreddit() {
  forEach post type of subreddit {
    defaultTitle = title of post?
    linkCount = linksFound in post
    forEach (link, index)
      if (!validateSupergenUrl(link.href))
        continue;
      
      ensureSupergenAdded(defaultTitle, linkCount, link.href)
  }    
      
  foreEach link type of subreddit {
    if (!validateSupergenUrl(link.href))
      continue;
  }
}
    
