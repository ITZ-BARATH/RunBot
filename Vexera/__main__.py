from Vexera import BOT

START = f"""
Bot Started!
"""




if __name__ == "__main__":
    BOT.run()
    with BOT:
       BOT.send_message(-1001693026740, START)
        
 
