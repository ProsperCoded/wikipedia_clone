import re
import sys
Representation = {"strick through":"[ ,\n]~~.+~~[ ,\n]", 
                  "bold":"[ ,\n]\*\*.+\*\*[ ,\n]",
                  "italic":"[ ,\n]\*.+\*[ ,\n]|[ ,\n]\_.+\_[ ,\n]",
                  "bold and italic":"[ ,\n]\*\*\*.+\*\*\*[ ,\n]",  
                    "link":"[ ,\n]\[.+\]\(.+\)[ ,\n]",
                    "image": "[ ,\n]\!\[.+\](.+)[ ,\n]",
                    "bullet list":"\* .+\n|\- .+\n",
                    "heading":"[ ,\n]\#{1,6} .+\n"}
# Necessary gap put by user for tag to be valid
gap = '[ ,\n]'
re_sep = ".+"
def strick_through(tag_item):
    tag_item = tag_item.strip("~~")
    tag_item = " "+tag_item+" "
    return "<s>" + tag_item + "</s>"
def bold(tag_item):
    tag_item = tag_item.strip('**')
    tag_item = " "+tag_item+" "
    return "<b>" + tag_item +"</b>"
def italic(tag_item):
    tag_item = tag_item.strip("*")
    tag_item = " "+tag_item+" "
    return "<i>" + tag_item + "</b>"
def bold_and_italic(tag_item):
    tag_item = tag_item.strip("***")
    tag_item = " "+tag_item+" "
    return "<i><b>" + tag_item +"</b></i>"
def link(tag_item):
    tag_item = tag_item.lstrip('[')
    tag_item = tag_item.rstrip(')')
    tag_items = tag_item.split("](")
    value = tag_items[0]
    
    href = '"'+ tag_items[1]+ '"'
    return f"<a href={href}>{value}</a>"
def bullet_list(tag_item):
    tag_item = tag_item.lstrip('-')
    tag_item = tag_item.lstrip('*')
    return f"<ul><li>{tag_item}</li></ul>"
def heading(tag_item):
    tags = re.compile("#").match(tag_item).group()
    n = tags.count("#")
    tag_item = tag_item.lstrip("#")
    return f"<h{n}>{tag_item}<h{n}>"


def convert_to_html(file=None,string=""):
    if  file and file.readable():
        string:str = file.read()
    string = '<p>\n'+ string +"\n</p>"
    for key in Representation.keys():
        value = Representation[key]
        
        pattern = re.compile(value)
        results = pattern.findall(string)
        value = value.removeprefix(gap).removesuffix(gap)
        start_pos = 0
        if results != []:
            for result in results:
                match = pattern.search(string,pos=start_pos)
                result:str = result.strip()
                match key:
                    case "strick through":
                        result = strick_through(result)
                    case "bold":
                        result = bold(result)
                    case "bold and italic":
                        result = bold_and_italic(result)
                    case "link":
                        result = link(result)
                    case "bullet list":
                        result = bullet_list(result)
                    case "heading":
                        result = heading(result)
                print(result)
                
                start_index = match.start()
                end_index = match.end()
                string = string[:start_index] +result+string[end_index:]
                start_pos = end_index
                
    return string
if __name__ == "__main__" and len(sys.argv) >= 0:
    # src = sys.argv[1]
    # des = sys.argv[2]
    src = "python.md"
    des = "python.html"
    import pathlib
    path = pathlib.Path(des)
    if not path.exists():
        path.touch()
    with open(des,'w') as file:
        HTML = convert_to_html(open(src,'r'))
        file.write(HTML)


