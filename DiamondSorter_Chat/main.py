from MainContactsWidget import MainContactsWidget
from utils import ReceiveMessageEvent
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication
from loginWidget import LoginWidget
import sys
import DataManager

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_widget = LoginWidget()
    main_window = MainContactsWidget()
    
    def postEvent(data, fromGroup=False):
        event = ReceiveMessageEvent(data, fromGroup)
        for widget in QApplication.topLevelWidgets():
            QCoreApplication.sendEvent(widget, event)
    
    def setuserinfoSuccess():
        global main_window
        print("in setuserinfoSuccess")
        DataManager.db_manager.add_friend_signal.connect(main_window.AddFriend)
        DataManager.db_manager.delete_friend_signal.connect(main_window.deleteFriend)
        DataManager.db_manager.add_group_signal.connect(main_window.AddGroup)
        DataManager.db_manager.delete_group_signal.connect(main_window.deleteGroup)
        DataManager.db_manager.add_group_message_signal.connect(lambda data: postEvent(data, True))
        DataManager.db_manager.add_friend_message_signal.connect(lambda data: postEvent(data, False))
        
        def on_receive_message(data):
            print("on_receive_message", data)
            if "group_id" not in data:
                DataManager.db_manager.add_friend_message(data["content"], data["username"], data["username"], data["timestamp"])
            else:
                DataManager.db_manager.add_group_message(data["content"], data["username"], data["group_id"], data["timestamp"])
        
        DataManager.dataManager.websocket_thread.receive_message.connect(on_receive_message)
    
    DataManager.dataManager.setUserInfoSuccess.connect(setuserinfoSuccess)
    
    def on_login_success():
        global main_window
        print("in on_login_success")
        main_window.setUserInfo()
        print(main_window, "username:", DataManager.dataManager.username, "nickname:", DataManager.dataManager.nickname, "session_id:", DataManager.dataManager.session_id)
        login_widget.close() 
        if main_window.isHidden():
            main_window.show()
        else:
            main_window.activateWindow()
    
    def new_user_join(data):
        DataManager.db_manager.addGroupMember(data["group_id"], data["username"], data["nickname"], data.get("avatar", None))
    
    DataManager.dataManager.websocket_thread.new_user_join_group.connect(new_user_join)
    DataManager.dataManager.websocketConnected.connect(on_login_success)
    
    login_widget.show()
    sys.exit(app.exec_())