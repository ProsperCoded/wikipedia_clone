function show_suggestions () {
  search_bar = document.getElementsByClassName('search')[0]
  generate_suggestions(search_bar.value)
}
function generate_suggestions (compare) {
  let listed = document.getElementsByClassName('entry_list')
  store = []
  
  for (let entry = 0; entry < listed.length; entry++) {
    anchor = listed[entry].children[0]
    if (anchor.text.toLowerCase().includes(compare.toLowerCase())) {
      listed[entry].style.display = 'block'
    } else {
      listed[entry].style.display = 'none'
    }
  }
}
function set_hrefs(anchors){
    for (let i=0 ;i< anchors.length; i++){
        value = anchors[i].text
        anchors[i].href = value
    }
}