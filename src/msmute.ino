#include <BleKeyboard.h>
#include <ezButton.h>

BleKeyboard bleKeyboard;

ezButton button1(23);
ezButton button2(22);
ezButton button3(21);
ezButton button4(19);

void setup()
{
  Serial.begin(115200);
  Serial.println("Starting BLE work!");
  bleKeyboard.begin();
  button1.setDebounceTime(50);
  button2.setDebounceTime(50);
  button3.setDebounceTime(50);
  button4.setDebounceTime(50);
}

void loop()
{
  button1.loop();
  button2.loop();
  button3.loop();
  button4.loop();

  if (bleKeyboard.isConnected())
  {

    if (button1.isPressed())
    {
      Serial.println("The button 1 is pressed");
      Serial.println("Sending Play/Pause media key...");
      bleKeyboard.write(KEY_MEDIA_PLAY_PAUSE);
      delay(10);
    }
    if (button2.isPressed())
    {
      Serial.println("The button 2 is pressed");
      Serial.println("Sending mute/unmute command...");
      bleKeyboard.press(KEY_LEFT_CTRL);
      bleKeyboard.press(KEY_LEFT_ALT);
      bleKeyboard.press(KEY_LEFT_GUI);
      bleKeyboard.press('m');
      delay(10);
      bleKeyboard.releaseAll();
    }
    if (button3.isPressed())
    {
      Serial.println("The button 3 is pressed");
      Serial.println("Sending camera on/off command...");
      bleKeyboard.press(KEY_LEFT_CTRL);
      bleKeyboard.press(KEY_LEFT_ALT);
      bleKeyboard.press(KEY_LEFT_GUI);
      bleKeyboard.press('o');
      delay(10);
      bleKeyboard.releaseAll();
    }
    if (button4.isPressed())
    {
      Serial.println("The button 4 is pressed");
      Serial.println("Sending leave meeting command...");
      bleKeyboard.press(KEY_LEFT_CTRL);
      bleKeyboard.press(KEY_LEFT_ALT);
      bleKeyboard.press(KEY_LEFT_GUI);
      bleKeyboard.press('h');
      delay(10);
      bleKeyboard.releaseAll();
    }
  }
}
