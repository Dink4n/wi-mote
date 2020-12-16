import React from "react";
import { Grid } from "semantic-ui-react";
import { FaVolumeMute } from "react-icons/fa";
import { FaExpandArrowsAlt } from "react-icons/fa";
import { AwesomeButton } from "react-awesome-button";
import { handleKeyPress } from "../api";

export const Utilities = () => {
	return (
		<Grid>
			<Grid.Row columns={2}>
				<Grid.Column>
					<AwesomeButton
						type="primary"
						onPress={() => handleKeyPress("toggle_mute")}
					>
						<FaVolumeMute size={20} />
					</AwesomeButton>
				</Grid.Column>
				<Grid.Column>
					<AwesomeButton
						type="primary"
						onPress={() => handleKeyPress("fullscreen")}
					>
						<FaExpandArrowsAlt size={20} />
					</AwesomeButton>
				</Grid.Column>
			</Grid.Row>
		</Grid>
	);
};
