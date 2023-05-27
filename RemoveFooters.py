for i in range (37,151):
    with open("C:/Users/User/Desktop/git trial/"+str(i)+".txt", "r",encoding='utf-8') as fp:
        lines = fp.readlines()

    with open("C:/Users/User/Desktop/git trial/"+str(i)+".txt", "w", encoding='utf-8',) as fp:
        for line in lines:
            if line.strip(
                    "\n") != '        /.td-container  ':  # or line.strip("\n")!= ' We provide intelligence, accelerate innovation and implement technology with extraordinary breadth and depth global insights into the big data,data-driven dashboards, applications development, and information management for organizations through combining unique, specialist services and high-lvel human expertise. Contact us:  © All Right Reserved, Blackcoffer(OPC) Pvt. Ltd ':
                fp.write(line)

    with open("C:/Users/User/Desktop/git trial/"+str(i)+".txt", "r", encoding='utf-8' ) as fp:
        lines = fp.readlines()

    with open("C:/Users/User/Desktop/git trial/"+str(i)+".txt", "w", encoding='utf-8') as fp:
        for line in lines:
            if line.strip(
                    "\n") != ' We provide intelligence, accelerate innovation and implement technology with extraordinary breadth and depth global insights into the big data,data-driven dashboards, applications development, and information management for organizations through combining unique, specialist services and high-lvel human expertise. Contact us:  © All Right Reserved, Blackcoffer(OPC) Pvt. Ltd ':
                fp.write(line)