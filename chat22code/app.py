from terminal import Terminal
from chat_interface import ChatInterface
from model_selection import ModelSelection
from chat_history import ChatHistory
from token_management import TokenManagement
from mode_selection import ModeSelection
from notifications import Notifications
from offline_mode import OfflineMode
from performance_monitoring import PerformanceMonitoring
from privacy_security import PrivacySecurity
from risks_mitigations import RisksMitigations
from shared_dependencies import SharedDependencies
from software_updates import SoftwareUpdates
from task_handling import TaskHandling
from ui_ux import UIUX
from web_endpoint import WebEndpoint


class App:
    def __init__(self):
        self.terminal = Terminal()
        self.chat_interface = ChatInterface()
        self.model_selection = ModelSelection()
        self.chat_history = ChatHistory()
        self.token_management = TokenManagement()
        self.mode_selection = ModeSelection()
        self.notifications = Notifications()
        self.offline_mode = OfflineMode()
        self.performance_monitoring = PerformanceMonitoring()
        self.privacy_security = PrivacySecurity()
        self.risks_mitigations = RisksMitigations()
        self.shared_dependencies = SharedDependencies()
        self.software_updates = SoftwareUpdates()
        self.task_handling = TaskHandling()
        self.ui_ux = UIUX()
        self.web_endpoint = WebEndpoint()

    def run(self):
        while True:
            user_input = input('Enter a command: ')
            if user_input == 'exit':
                break
            elif user_input == 'display terminal':
                self.terminal.display_terminal()
            elif user_input == 'display chat interface':
                self.chat_interface.display_chat_interface()
            elif user_input == 'select model':
                self.model_selection.select_model()
            elif user_input == 'start new session':
                self.chat_history.start_new_session()
            elif user_input == 'view chat history':
                self.chat_history.view_past_history()
            elif user_input == 'display token count':
                self.token_management.display_token_count()
            elif user_input == 'toggle mode':
                self.mode_selection.toggle_mode()
            elif user_input == 'send responses to endpoint':
                self.web_endpoint.send_responses_to_endpoint()
            elif user_input == 'support ongoing conversations':
                self.continuous_interaction.support_ongoing_conversations()
            elif user_input == 'capture errors':
                self.error_handling.capture_errors()
            elif user_input == 'log errors':
                self.error_handling.log_errors()
            elif user_input == 'set milestones':
                self.milestones_timeline.set_milestones()
            elif user_input == 'set timeline':
                self.milestones_timeline.set_timeline()
            elif user_input == 'mitigate complexity':
                self.risks_mitigations.mitigate_complexity()
            elif user_input == 'ensure security':
                self.risks_mitigations.ensure_security()
            elif user_input == 'manage dependencies':
                self.shared_dependencies.manage_dependencies()
            elif user_input == 'auto update':
                self.software_updates.auto_update()
            elif user_input == 'handle tasks':
                self.task_handling.handle_tasks()
            elif user_input == 'create user-friendly design':
                self.ui_ux.create_user_friendly_design()
            else:
                print('Invalid command. Please try again.')


if __name__ == '__main__':
    app = App()
    app.run()
