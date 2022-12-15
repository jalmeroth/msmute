if application "Microsoft Teams" is running then
	# Remember the current application in focus
	set old to (path to frontmost application as text)
	log old
	
	activate application "Microsoft Teams"
	set new to (path to frontmost application as text)
	log new
	
	tell application "System Events"
		tell process "Microsoft Teams"
			# first round may opens history
			# lets close it in the second run
			repeat 2 times
			# Microsoft Teams Notification-Window is no good
			set win_names to (name of every window where name does not contain "Microsoft Teams Notification")
				log win_names
				# bruteforce which window to close
				# might opens history view
				repeat with win_name in win_names
					# let's try to switch current window
					click menu item (win_name) of menu "Window" of menu bar 1
					tell application "System Events" to keystroke "H" using {command down, shift down}
				end repeat
			end repeat
		end tell
	end tell
	
	if old is not new then
		activate application old
	end if
end if