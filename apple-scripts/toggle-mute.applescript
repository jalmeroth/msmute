if application "Microsoft Teams" is running then
	# Remember the current application in focus
	set old to (path to frontmost application as text)
	log old
	
	activate application "Microsoft Teams"
	set new to (path to frontmost application as text)
	log new
	
	tell application "System Events"
		tell process "Microsoft Teams"
			set win_names to name of every window
			log win_names
			if (count win_names) > 1 then
				# flip windows to get a focused window
				click menu item (item 2 of win_names) of menu "Window" of menu bar 1
				click menu item (item 1 of win_names) of menu "Window" of menu bar 1
			end if
			tell application "System Events" to keystroke "M" using {command down, shift down}
		end tell
	end tell
	
	if old is not new then
		activate application old
	end if
end if