from infra.base import Base

class HomePage(Base):

    permission_allow_location_button = ('id', 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
    transport_icon = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]')
    alertTitle = ('id', 'android:id/alertTitle')
    alertMessage = ('id', 'android:id/message')
    alertButton = ('id', 'android:id/button1')

    def click_allow_location(self):
        self.click(self.permission_allow_location_button)

    def click_transport_icon(self):
        self.click(self.transport_icon)

    def get_alert_title(self):
        return self.get_text(self.alertTitle)

    def get_alert_message(self):
        return self.get_text(self.alertMessage)

    def click_alert_ok_button(self):
        self.click(self.alertButton)