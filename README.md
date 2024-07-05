NIR WORLD FOOD GRAPH MODEL
----------------------------

MAIN FILE : ll.py

----------------------------

Created a Graph DS and plotted it for visual representation

Each node in a graph denotes a city or village in the earth

Right now I have only taken dummy data and created 10 nodes around a center of reference

As the Earth is spherical we can construct a connected graph connecting each particular recognized town or village to each other
and as the earth is spherical the networks will be circular graph representing earth network

Each node has its neighbours which needs to maintained with a small radius and only store a limited neighbours thus saving space
Each node will have Food Consumption and Food Production rate data

As the nodes must create new edges with outer circle cities or village i have hardcoded to create random node within the angle (0 to 180)degree.

Further we will recognize the maximum production place and maximum scarcity place and create a next node passing to reach each scarcity area in the graph and calculate the data analysis for the problems that might occur
the expenditure, the food expiry limitation to create a efficient supply overall the world.

-----------------------------

Further Updates:

As i have completed the basic node creation,addition of nodes and edges now I am working on availing the appropriate data to fill in the node data
After the data is completed first I will build network for a country first
then I will connect continents
then we can analyse the data about the rate of consumption and production of food and water in each town and villages.
Then we can look into the existing supplies coming and going out from the place itself and how the place survives.
We will also gain the amount of wastage of food in the place.

----------------------------------

# AIM

Creating World Wide Zero Food Scaricity Solution For Future Generations
The idea works just like the NETWORK BUT I AM ADDING UP THE ALGORITHMS TO CREATE A MORE EFFICIENT SOLUTION AND AVOID CONFLITS IN THE NETWORK.
Visualizing the viability using the graph DS
Trying to Calculate the overall data and actions required per day/week

first imagine circular linked list
now imagine circular linked list in spherical representation with earth model
now you can see whole world is circularly connected with each city or village being a node and connected to each other

now imagine producer consumer problem
put that in food production and consumption
now every city is consuming x quantity of food per day and have y quantity of scarcity
some city might also have 0 percent scarcity (lets assume for now)
there is z quantity of wastage of raw food in every city

now apply multithreading concept where each node in linked list is passing food at the same time which it has to its next neighbour which it has in its food bank at the same time
you can imagine right, place which had 0 quantity of food received food right and one who donated also received with his previous node.

but still the scarcity is not over 
a area needs suppose 20 percent of food at least to stop scarcity
now when we pass on food to immediate neighbor each day we can see even if some areas doesn't received food in day1 the food which was left in that day will be passed on to next destination
after food will be consumed while the food production will also be somewhere.

one day will come when there will be decrease in the food scarcity as the food is been delivered in all parts and y quantity of scarcity will decrease now our model can slow down with less consumption of other resources and maintain the solution

since there is no consumption in an area that's why food gets rotten but if the flow of food grows near consumer then the food bank consumption will increase and wastage will decrease

If food gets rotten you can still supply water which does rott i mean clean water can be passed on for some time to create a base condition for this model to work perfectely

we need to analyse the base condition for this model to work using our Graph virtually and create such situation in the physical world and work accordingly to the Graph generated prediction and analysis to solve the world wide food scarcity problem.

I know there are many flaws in the Idea but After the model is over we can predict the base condition needed for the production and consumption and connectivity problems can be solved too. We will get enough data to work on and maybe one day we will have ZERO FOOD SCARCITY IN THE WHOLE WORLD...............

FEEL FREE TO WORK ON THIS IDEA ON YOUR OWN.
AS WE MIGHT NOT BE ABLE TO ACHIEVE SOME BASE CASES BUT SURELY OUR FUTURE GENERATIONS CAN.
AND I HOPE WE OURSELVES ACHIEVE THE BASE CASE.

ALL FOR THE FUTURE GENERATION.

---------------------------------------
# FOR EVERYONE WHO NEEDS TO HEAR THIS

Respected Readers, 
 
Please Listen to my proposal for once. 
 
Basic needs of humans are the only thing someone needs to survive and food is the only one you might 
only need to survive. 
 
People who don’t get food cannot survive. 
Lets see into this problem now. 
 
I am designing a way to solve the food scarcity problem in the world. 
 
Suppose there is scarcity of food in a village x and as we know if you take a place as a circle center you 
will find many other villages inside its perimeter so let’s take an example of any village y in the perimeter 
which has food with them they can share the food with village x right. But sharing will create scarcity in 
the village y too if not enough after sharing food which still creates a problem. 
 
Now let’s find a Village from village y opposite to the direction of village x and search for some village and
see if they have food. 
If sharing the food from the village still creates scarcity then let’s again search in the same way until we 
find a village which has sufficient food who even after sharing can have sufficient food. 
 
Now after finding it we can transport the food to the nearest village to the inner and this is important if the 
village who is getting food had some food before they could have shared it with the village in its inner 
circle which had scarcity and this way you can solve the food scarcity problem. As we are taking a circle 
model we will have multiple ways to achieve this. 
The problem which arises here is transportation as a single village must have to transport food a number 
of times to its next village as the transportation is point to point where before the model was a single trip. 
So some organizations should help us in this field as this is the only problem in this situation. But if we 
use this food solution with vehicle fuel we can solve it too. I am still trying to draw the layout of the 
solution’s problems but still with the help of some organization we can fix it until we create a solution for it.
I am making a chakravyuh model and fitting it into this solution model for now for vehicle problems. 
 
a village x will get food which village y had and solve food scarcity problem for village x and village y who 
donated their food will be helped by the village around him and so on goes on with the radius. If villages 
are notified before time that they will get food they can share food immediately and food will reach 
eventually to both villages. 
more outside the village from the center will have more trips because the food is being distributed from 
outside the circle to inside the circle and has to go through it but being a circle the division will decrease 
as we have a 360° division load for the village. 
 
Another problem is still the food will rot as we are sharing the same food over and over again from village 
to village so we need to look into this problem too. My solution is just a fast way of transportation of food if
availability is there. If the trips are faster we will get no problems in food scarcity and some day the people
of the area will eventually be prepared enough I believe so. If each place separates a food donation 
storage and operates by passing on the food it will be like a village will donate to its inner circle and outer 
circle village will donate to us making it a never ending process and thus the problem solved in itself. 
 
Longer the trips the more the food might rot which is still bad so in this way we can transport food from 
any part of the world to another in a better way by not transporting a food of a certain part to another but 
sharing from immediate nearby places. If every city and villages will have this system built and properly 
designed no village in the world will go empty stomach at night. The village won't need to preserve the 
food which might also lead to rotten food supplies. Instead they can share the food and get it replaced by 
another village. 
 
People might not be eager to donate their food and get a replacement for that but it is a good start of 
changing views on this topic. 
 
People waste food. It doesn't need to be bad, disposing food in the garden can be good compost where 
you can grow new vegetables. 
We people donate the wasted food to other peoples but i don't want to make it that way food can rot in a 
way which can be harmful to an unhealthy body. Instead a way of sharing raw food is better than sharing 
wasted food. And if even if this doesn't create an idea please listen to this "Don't fear as Whatever we 
donated will come back our way." 
 
All I want to say is God has made earth spherical for a reason which we shouldn't ignore and use it to 
fulfill our duty and needs as a human. 
 
I come from Nepal, Nepal is still largely an agrarian nation with around 62% of total population engaged in
agriculture and we still suffer food scarcity, same goes with other of my neighbouring countries and all 
other countries around our planet. 
 
I am a student who would like to solve the problem for our planet's future.
 
Yours Sincerely, 
Jay Mehta
