# tw2lint
Basic code linter for TW2 files

The idea for this is that I'm working on large TW2 files (Twine
games).

It's hard to keep consistency around the files, so I'm working on
making something that will spot problems with the file, such as
nodes that can't be reached or exited from, nodes where there are
formatting errors, and so on.

## Overall Planned Features

Draw a graph of the game showing all nodes and links
(optionally with link labels) in Graphviz format.

Reason over the graph, and identify problems.

## MoSCoW:

### Features:
M:
* Identify passages that are unreachable (no incoming links); 
* Identify invalid links - the ones where the target doesn't exist;
* Identify unexitable nodes - ones with no exit links; *

NB: * this will be hard from the graphviz output unless we print a
node at least once irrespective of the number of exit links - we
need to print a box for each passage when we encounter it. If no
exit links, then just don't do any exit links. This will cause it
to rank at the right of the graph)   Unreachable passages will rise
to the left

S:
* Draw a map of the game;
* Identify mismatched braces;
* Identify formatting that's likely wonky - new lines in [[ ]] pairs;
* Educate quotes;
* Identify missing format or other metadata;
* Identify missing include files;

C:
* Identify missing external image/media links;
* Optionally add <x,y> pairs so loading into Twine2 will work;

W:
* Actually compile

