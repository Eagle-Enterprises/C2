// Call the library
#include "mavlink.h"

// Mavlink variables
unsigned long previousMillisMAVLink = 0;     // will store last time MAVLink was transmitted and listened
unsigned long next_interval_MAVLink = 1000;  // next interval to count

// Launch the serial port in setup
void setup() {
  // MAVLink interface start
  
  Serial.begin(57600);
  Serial.swap();
}
// Loop your program
void loop() {
  // MAVLink config
  /* The default UART header for your MCU */ 
  int sysid = 65;                   ///< ID 20 for this airplane. 1 PX, 255 ground station
  int compid = 158;                ///< The component sending the message
  int type = MAV_TYPE_QUADROTOR;   ///< This system is an airplane / fixed wing
 
  // Define the system type, in this case an airplane -> on-board controller
  uint8_t system_type = MAV_TYPE_GENERIC;
  uint8_t autopilot_type = MAV_AUTOPILOT_INVALID;
 
  uint8_t system_mode = MAV_MODE_PREFLIGHT; ///< Booting up
  uint32_t custom_mode = 0;                 ///< Custom mode, can be defined by user/adopter
  uint8_t system_state = MAV_STATE_STANDBY; ///< System ready for flight

  uint16_t test_seq = 1234;

  // Initialize the required buffers
  mavlink_message_t msg;
  mavlink_message_t msg1;

  uint8_t buf[MAVLINK_MAX_PACKET_LEN];
 
  // Pack the message
  mavlink_msg_heartbeat_pack(1,0, &msg, type, autopilot_type, system_mode, custom_mode, system_state);
 
  // Copy the message to the send buffer
  uint16_t len = mavlink_msg_to_send_buffer(buf, &msg);
 
  // Send the message with the standard UART send function
  // uart0_send might be named differently depending on
  // the individual microcontroller / library in use.
  unsigned long currentMillisMAVLink = millis();
  if (currentMillisMAVLink - previousMillisMAVLink >= next_interval_MAVLink) {
    // Timing variables
    previousMillisMAVLink = currentMillisMAVLink;
    Serial.write(buf, len);
    delay(1000);
  }


  uint8_t target_system = 249;
  uint8_t target_component = 12;
  uint16_t command = 31000;
  uint8_t confirmation = 0;
  float uwb_distance = 75.5;

  // TEST message 1
  mavlink_msg_command_long_pack(sysid,
                                compid,
                                &msg1,
                                target_system,
                                target_component,
                                command,
                                confirmation,
                                uwb_distance,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0);


  len = mavlink_msg_to_send_buffer(buf, &msg1);

  currentMillisMAVLink = millis();
  if (currentMillisMAVLink - previousMillisMAVLink >= next_interval_MAVLink) {
    // Timing variables
    previousMillisMAVLink = currentMillisMAVLink;

    Serial.write(buf, len);

    delay(1000);
  }

  // Check reception buffer
  //comm_receive();
}