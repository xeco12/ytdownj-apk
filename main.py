"""
YTDown - YouTube Downloader
WebView tabanlı Kivy Android Uygulaması
"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from android.runnable import run_on_ui_thread
from jnius import autoclass

# Android WebView sınıfları
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
WebSettings = autoclass('android.webkit.WebSettings')
PythonActivity = autoclass('org.kivy.android.PythonActivity')
LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')
LinearLayout = autoclass('android.widget.LinearLayout')


class WebViewApp(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.create_webview, 0)

    @run_on_ui_thread
    def create_webview(self, *args):
        activity = PythonActivity.mActivity

        # WebView oluştur
        webview = WebView(activity)
        webview.setWebViewClient(WebViewClient())

        # Ayarlar
        settings = webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setLoadWithOverviewMode(True)
        settings.setUseWideViewPort(True)
        settings.setBuiltInZoomControls(False)
        settings.setDisplayZoomControls(False)
        settings.setSupportZoom(False)

        # Layout
        layout = LinearLayout(activity)
        layout.setOrientation(LinearLayout.VERTICAL)
        params = LayoutParams(
            LayoutParams.MATCH_PARENT,
            LayoutParams.MATCH_PARENT
        )
        layout.addView(webview, params)
        activity.setContentView(layout)

        # HTML içeriğini yükle
        webview.loadUrl("file:///android_asset/index.html")


class YTDownApp(App):
    def build(self):
        return WebViewApp()


if __name__ == '__main__':
    YTDownApp().run()
