import React from "react";
import { AwesomeButton } from "react-awesome-button";
import { MdFastForward, MdFastRewind, MdPause } from "react-icons/md";
import { Grid } from "semantic-ui-react";
import { handleKeyPress } from "../api";

export const Player = () => {
	return (
		<Grid columns="equal">
			<Grid.Row>
				<Grid.Column>
					<AwesomeButton
						size="small"
						type="secondary"
						onPress={() => handleKeyPress("rewind")}
					>
						<MdFastRewind size={20} />
					</AwesomeButton>
				</Grid.Column>
				<Grid.Column>
					<AwesomeButton
						size="small"
						type="secondary"
						onPress={() => handleKeyPress("pause")}
					>
						<MdPause size={20} />
					</AwesomeButton>
				</Grid.Column>
				<Grid.Column>
					<AwesomeButton
						size="small"
						type="secondary"
						onPress={() => handleKeyPress("forward")}
					>
						<MdFastForward size={20} />
					</AwesomeButton>
				</Grid.Column>
			</Grid.Row>
		</Grid>
	);
};
