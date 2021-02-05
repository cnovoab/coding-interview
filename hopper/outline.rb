class Heading
    attr_accessor :weight, :text
    def initialize(weight, text)
        @weight = weight
        @text = text
    end
end

class Node
    attr_accessor :heading, :children
    def initialize(heading, children)
        @heading = heading
        @children = children
    end
end

def to_outline(headings)
    return if headings.empty?

    current = headings.shift
    Node.new(current, to_outline(headings.map { |h| h.weight > current.weight }))
    # Node.new(Heading.new(0, ""), [Node.new(Heading.new(1,'Peroli'), [])])
end

def parse(record)
    (hlevel, text) = record.split(" ", 2)
    Heading.new(hlevel[1..-1].to_i, text.strip)
end

def to_html(node)
    if node.children.length == 0
        child_html = ""
    else
        child_html = "<ol>" +
            node.children.map { |child| "<li>" + to_html(child) + "</li>" }.join("\n") +
            "</ol>"
    end

    if node.heading.text == ""
        child_html
    else
        node.heading.text + "\n" + child_html
    end
end

# headings = ARGF.readlines.map { |line| parse(line) }
headings = [parse(ARGV.join(' '))]
puts "Headings: #{headings.inspect}"
outline = to_outline(headings)

puts to_html(outline)

