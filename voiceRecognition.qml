import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.3

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("AGL Application Demo Test")
    color: "#316e8f"

    ColumnLayout {
        Button {
            id: control
            text: qsTr("Press to speak")

            contentItem: Text {
                text: control.text
                font: control.font
                opacity: enabled ? 1.0 : 0.3
                color: control.down ? "#f5f5f5" : "#0b0224"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                elide: Text.ElideRight
            }

            background: Rectangle {
                color: control.down ? "#0b0224" : "#eb8c10"
                implicitWidth: 100
                implicitHeight: 40
                opacity: enabled ? 1 : 0.3
                border.color: control.down ? "#0b0224" : "#eb8c10"
                border.width: 1
                radius: 2
            }

            onClicked: {
                var output = voiceRecognizer.record_sound_button()
                console.log(output)
                thetext.text = output
            }
        }

        Text {
            id: thetext
            text: "sample"
            font.family: "arial"
            font.pointSize: 16
            color: "white"
        }
    }
}
