#!/usr/bin/python3

# Module documentation
# This script generates a JSON file containing all tasks from all employees.

import json
from collections import defaultdict

# Dictionary to store tasks for each user
tasks = defaultdict(list)

# Sample data
users = {
    "1": ["Bret", "delectus aut autem", False, "quis ut nam facilis et officia qui", False, "fugiat veniam minus", False, "et porro tempora", True, "laboriosam mollitia et enim quasi adipisci quia provident illum", False, "qui ullam ratione quibusdam voluptatem quia omnis", False, "illo expedita consequatur quia in", False, "quo adipisci enim quam ut ab", True, "molestiae perspiciatis ipsa", False, "illo est ratione doloremque quia maiores aut", True, "vero rerum temporibus dolor", True, "ipsa repellendus fugit nisi", True, "et doloremque nulla", False, "repellendus sunt dolores architecto voluptatum", True, "ab voluptatum amet voluptas", True, "accusamus eos facilis sint et aut voluptatem", True, "quo laboriosam deleniti aut qui", True, "dolorum est consequatur ea mollitia in culpa", False, "molestiae ipsa aut voluptatibus pariatur dolor nihil", True, "ullam nobis libero sapiente ad optio sint", True],
    "2": ["Antonette", "suscipit repellat esse quibusdam voluptatem incidunt", False, "distinctio vitae autem nihil ut molestias quo", True, "et itaque necessitatibus maxime molestiae qui quas velit", False, "adipisci non ad dicta qui amet quaerat doloribus ea", False, "voluptas quo tenetur perspiciatis explicabo natus", True, "aliquam aut quasi", True, "veritatis pariatur delectus", True, "nesciunt totam sit blanditiis sit", False, "laborum aut in quam", False, "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis", True, "repudiandae totam in est sint facere fuga", False, "earum doloribus ea doloremque quis", False, "sint sit aut vero", False, "porro aut necessitatibus eaque distinctio", False, "repellendus veritatis molestias dicta incidunt", True, "excepturi deleniti adipisci voluptatem et neque optio illum ad", True, "sunt cum tempora", False, "totam quia non", False, "doloremque quibusdam asperiores libero corrupti illum qui omnis", False, "totam atque quo nesciunt", True],
    "3": ["Samantha", "aliquid amet impedit consequatur aspernatur placeat eaque fugiat suscipit", False, "rerum perferendis error quia ut eveniet", False, "tempore ut sint quis recusandae", True, "cum debitis quis accusamus doloremque ipsa natus sapiente omnis", True, "velit soluta adipisci molestias reiciendis harum", False, "vel voluptatem repellat nihil placeat corporis", False, "nam qui rerum fugiat accusamus", False, "sit reprehenderit omnis quia", False, "ut necessitatibus aut maiores debitis officia blanditiis velit et", False, "cupiditate necessitatibus ullam aut quis dolor voluptate", True, "distinctio exercitationem ab doloribus", False, "nesciunt dolorum quis recusandae ad pariatur ratione", False, "qui labore est occaecati recusandae aliquid quam", False, "dolorum est consequatur ea mollitia in culpa", False, "molestiae ipsa aut voluptatibus pariatur dolor nihil", True, "ullam nobis libero sapiente ad optio sint", True],
    "4": ["Karianne", "odit optio omnis qui sunt", True, "et placeat et tempore aspernatur sint numquam", False, "doloremque aut dolores quidem fuga qui nulla", True, "voluptas consequatur qui ut quia magnam nemo esse", False, "fugiat pariatur ratione ut asperiores necessitatibus magni", False, "rerum eum molestias autem voluptatum sit optio", False, "quia voluptatibus voluptatem quos similique maiores repellat", False, "aut id perspiciatis voluptatem iusto", False, "doloribus sint dolorum ab adipisci itaque dignissimos aliquam suscipit", False, "ut sequi accusantium et mollitia delectus sunt", False, "aut velit saepe ullam", False, "praesentium facilis facere quis harum voluptatibus voluptatem eum", False, "sint amet quia totam corporis qui exercitationem commodi", True, "expedita tempore nobis eveniet laborum maiores", False, "occaecati adipisci est possimus totam", False, "sequi dolorem sed", True, "maiores aut nesciunt delectus exercitationem vel assumenda eligendi at", False, "reiciendis est magnam amet nemo iste recusandae impedit quaerat", False, "eum ipsa maxime ut", True, "tempore molestias dolores rerum sequi voluptates ipsum consequatur", True],
    "5": ["Kamren", "suscipit qui totam", True, "voluptates eum voluptas et dicta", False, "quidem at rerum quis ex aut sit quam", True, "sunt veritatis ut voluptate", False, "et quia ad iste a", True, "incidunt ut saepe autem", True, "laudantium quae eligendi consequatur quia et vero autem", True, "vitae aut excepturi laboriosam sint aliquam et et accusantium", False, "sequi ut omnis et", True, "molestiae nisi accusantium tenetur dolorem et", True, "nulla quis consequatur saepe qui id expedita", True, "in omnis laboriosam", True, "odio iure consequatur molestiae quibusdam necessitatibus quia sint", True, "facilis modi saepe mollitia", False, "vel nihil et molestiae iusto assumenda nemo quo ut", True, "nobis suscipit ducimus enim asperiores voluptas", False, "dolorum laboriosam eos qui iure aliquam", False, "debitis accusantium ut quo facilis nihil quis sapiente necessitatibus", True, "neque voluptates ratione", False, "excepturi a et neque qui expedita vel voluptate", False],
    "6": ["Leopoldo_Corkery", "explicabo enim cumque porro aperiam occaecati minima", False, "sed ab consequatur", False, "non sunt delectus illo nulla tenetur enim omnis", False, "excepturi non laudantium quo", False, "totam quia dolorem et illum repellat voluptas optio", True, "ad illo quis voluptatem temporibus", True, "praesentium facilis omnis laudantium fugit ad iusto nihil nesciunt", False, "a eos eaque nihil et exercitationem incidunt delectus", True, "autem temporibus harum quisquam in culpa", True, "aut aut ea corporis", True, "magni accusantium labore et id quis provident", False, "consectetur impedit quisquam qui deserunt non rerum consequuntur eius", False, "quia atque aliquam sunt impedit voluptatum rerum assumenda nisi", False, "cupiditate quos possimus corporis quisquam exercitationem beatae", False, "sed et ea eum", False, "ipsa dolores vel facilis ut", True, "sequi quae est et qui qui eveniet asperiores", False, "quia modi consequatur vero fugiat", False, "corporis ducimus ea perspiciatis iste", False, "dolorem laboriosam vel voluptas et aliquam quasi", False],
    "7": ["Elwyn.Skiles", "inventore aut nihil minima laudantium hic qui omnis", True, "provident aut nobis culpa", True, "esse et quis iste est earum aut impedit", False, "qui consectetur id", False, "aut quasi autem iste tempore illum possimus", False, "ut asperiores perspiciatis veniam ipsum rerum saepe", True, "voluptatem libero consectetur rerum ut", True, "eius omnis est qui voluptatem autem", False, "rerum culpa quis harum", False, "nulla aliquid eveniet harum laborum libero alias ut unde", True, "qui ea incidunt quis", False, "qui molestiae voluptatibus velit iure harum quisquam", True, "et labore eos enim rerum consequatur sunt", True, "molestiae doloribus et laborum quod ea", False, "facere ipsa nam eum voluptates reiciendis vero qui", False, "asperiores illo tempora fuga sed ut quasi adipisci", False, "qui sit non", False, "placeat minima consequatur rem qui ut", True, "consequatur doloribus id possimus voluptas a voluptatem", False, "aut consectetur in blanditiis deserunt quia sed laboriosam", True],
    "8": ["Maxime_Nienow", "explicabo consectetur debitis voluptates quas quae culpa rerum non", True, "maiores accusantium architecto necessitatibus reiciendis ea aut", True, "eum non recusandae cupiditate animi", False, "ut eum exercitationem sint", False, "beatae qui ullam incidunt voluptatem non nisi aliquam", False, "molestiae suscipit ratione nihil odio libero impedit vero totam", True, "eum itaque quod reprehenderit et facilis dolor autem ut", True, "esse quas et quo quasi exercitationem", False, "animi voluptas quod perferendis est", False, "eos amet tempore laudantium fugit a", False, "accusamus adipisci dicta qui quo ea explicabo sed vero", True, "odit eligendi recusandae doloremque cumque non", False, "ea aperiam consequatur qui repellat eos", False, "rerum non ex sapiente", True, "voluptatem nobis consequatur et assumenda magnam", True, "nam quia quia nulla repellat assumenda quibusdam sit nobis", True, "dolorem veniam quisquam deserunt repellendus", True, "debitis vitae delectus et harum accusamus aut deleniti a", True, "debitis adipisci quibusdam aliquam sed dolore ea praesentium nobis", True, "et praesentium aliquam est", False],
    "9": ["Delphine", "ex hic consequuntur earum omnis alias ut occaecati culpa", True, "omnis laboriosam molestias animi sunt dolore", True, "natus corrupti maxime laudantium et voluptatem laboriosam odit", False, "reprehenderit quos aut aut consequatur est sed", False, "fugiat perferendis sed aut quidem", False, "quos quo possimus suscipit minima ut", False, "et quis minus quo a asperiores molestiae", False, "recusandae quia qui sunt libero", False, "ea odio perferendis officiis", True, "quisquam aliquam quia doloribus aut", False, "fugiat aut voluptatibus corrupti deleniti velit iste odio", True, "et provident amet rerum consectetur et voluptatum", False, "harum ad aperiam quis", False, "similique aut quo", False, "laudantium eius officia perferendis provident perspiciatis asperiores", True, "magni soluta corrupti ut maiores rem quidem", False, "et placeat temporibus voluptas est tempora quos quibusdam", False, "nesciunt itaque commodi tempore", True, "omnis consequuntur cupiditate impedit itaque ipsam quo", True, "debitis nisi et dolorem repellat et", True],
    "10": ["Moriah.Stanton", "ut cupiditate sequi aliquam fuga maiores", False, "inventore saepe cumque et aut illum enim", True, "omnis nulla eum aliquam distinctio", True, "molestias modi perferendis perspiciatis", False, "voluptates dignissimos sed doloribus animi quaerat aut", False, "explicabo odio est et", False, "consequuntur animi possimus", False, "vel non beatae est", True, "culpa eius et voluptatem et", True, "accusamus sint iusto et voluptatem exercitationem", True, "temporibus atque distinctio omnis eius impedit tempore molestias pariatur", True, "ut quas possimus exercitationem sint voluptates", False, "rerum debitis voluptatem qui eveniet tempora distinctio a", True, "sed ut vero sit molestiae", False, "rerum ex veniam mollitia voluptatibus pariatur", True, "consequuntur aut ut fugit similique", True, "dignissimos quo nobis earum saepe", True, "quis eius est sint explicabo", True, "numquam repellendus a magnam", True, "ipsam aperiam voluptates qui", False]
}

# Iterate over users and tasks
for user_id, user_tasks in users.items():
    for task in user_tasks:
        tasks[user_id].append({"username": user_tasks[0], "task": task, "completed": False})

# Write tasks to JSON file
with open("todo_all_employees.json", "w") as file:
    json.dump(tasks, file, indent=4)


